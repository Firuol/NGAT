import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:ngat_practice/models/bank.dart';
import 'package:ngat_practice/screens/about_screen.dart';
import 'package:ngat_practice/screens/paper_screen.dart';
import 'package:ngat_practice/screens/session_screen.dart';
import 'package:ngat_practice/state/progress_store.dart';
import 'package:ngat_practice/theme/app_theme.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key, required this.bank, required this.progress});

  final QuestionBank bank;
  final ProgressStore progress;

  @override
  Widget build(BuildContext context) {
    final text = Theme.of(context).textTheme;
    final total = bank.all.length;
    final accuracy = progress.lifetimeAnswered == 0
        ? '—'
        : '${(progress.accuracy * 100).round()}%';

    return AnnotatedRegion<SystemUiOverlayStyle>(
      value: SystemUiOverlayStyle.light,
      child: Scaffold(
        body: ListView(
          padding: EdgeInsets.zero,
          children: [
            Container(
              decoration: const BoxDecoration(
                gradient: LinearGradient(
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                  colors: [Color(0xFF2E6E80), AppColors.forest, AppColors.forestDeep],
                ),
                borderRadius: BorderRadius.vertical(bottom: Radius.circular(36)),
              ),
              child: SafeArea(
                bottom: false,
                child: Padding(
                  padding: const EdgeInsets.fromLTRB(22, 12, 22, 28),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Container(
                        padding: const EdgeInsets.fromLTRB(10, 8, 14, 8),
                        decoration: BoxDecoration(
                          color: Colors.white,
                          borderRadius: BorderRadius.circular(18),
                        ),
                        child: Image.asset(
                          'assets/logo.png',
                          height: 54,
                          fit: BoxFit.contain,
                        ),
                      ),
                      const SizedBox(height: 22),
                      Text(
                        'Train for exam day.',
                        style: text.displaySmall?.copyWith(color: Colors.white),
                      ),
                      const SizedBox(height: 8),
                      Text(
                        '$total questions with worked answers, ready when you are.',
                        style: text.bodyMedium?.copyWith(
                          color: const Color(0xFFD5E7EC),
                        ),
                      ),
                      const SizedBox(height: 20),
                      Row(
                        children: [
                          _HeroStat(value: '${bank.exams.length}', label: 'Papers'),
                          const SizedBox(width: 10),
                          _HeroStat(
                            value: '${progress.lifetimeAnswered}',
                            label: 'Answered',
                          ),
                          const SizedBox(width: 10),
                          _HeroStat(value: accuracy, label: 'Accuracy'),
                        ],
                      ),
                    ],
                  ),
                ),
              ),
            ),
            const SizedBox(height: 22),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 22),
              child: Text('Papers', style: text.titleLarge),
            ),
            const SizedBox(height: 12),
            for (var i = 0; i < bank.exams.length; i++) ...[
              Padding(
                padding: const EdgeInsets.fromLTRB(22, 0, 22, 12),
                child: _PaperCard(
                  exam: bank.exams[i],
                  stats: progress.statsFor(bank.exams[i].id),
                  accent: _accents[i % _accents.length],
                  icon: _icons[i % _icons.length],
                  onTap: () {
                    Navigator.of(context).push(
                      MaterialPageRoute(
                        builder: (_) => PaperScreen(
                          exam: bank.exams[i],
                          progress: progress,
                        ),
                      ),
                    );
                  },
                ),
              ),
            ],
            const SizedBox(height: 8),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 22),
              child: Text('Quick drills', style: text.titleLarge),
            ),
            const SizedBox(height: 4),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 22),
              child: Text(
                'Ten questions. Explanation after every answer.',
                style: text.bodyMedium,
              ),
            ),
            const SizedBox(height: 14),
            SizedBox(
              height: 154,
              child: ListView(
                scrollDirection: Axis.horizontal,
                padding: const EdgeInsets.symmetric(horizontal: 22),
                children: [
                  _DrillCard(
                    label: 'Mixed',
                    icon: Icons.shuffle_rounded,
                    color: AppColors.forest,
                    onTap: () => _startDrill(context, null),
                  ),
                  for (final drill in _drills)
                    _DrillCard(
                      label: drill.$1,
                      icon: drill.$2,
                      color: drill.$3,
                      onTap: () => _startDrill(context, drill.$1),
                    ),
                ],
              ),
            ),
            const SizedBox(height: 22),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 22),
              child: _AboutTile(
                onTap: () {
                  Navigator.of(context).push(
                    MaterialPageRoute(builder: (_) => const AboutScreen()),
                  );
                },
              ),
            ),
            const SizedBox(height: 28),
          ],
        ),
      ),
    );
  }

  static const _accents = [
    AppColors.forest,
    Color(0xFF1A6B62),
    Color(0xFFC4842A),
  ];

  static const _icons = [
    Icons.menu_book_rounded,
    Icons.school_rounded,
    Icons.quiz_rounded,
  ];

  static const _drills = [
    ('Verbal', Icons.abc_rounded, Color(0xFF235562)),
    ('Quantitative', Icons.calculate_rounded, Color(0xFF1A6B62)),
    ('Logical', Icons.hub_rounded, Color(0xFF3D6B8C)),
    ('Analytical', Icons.account_tree_rounded, Color(0xFF8A6232)),
  ];

  void _startDrill(BuildContext context, String? section) {
    final pool = bank.all
        .where((question) => section == null || question.section == section)
        .toList()
      ..shuffle(Random());
    final questions = pool.take(10).toList();
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (_) => SessionScreen(
          title: section == null ? 'Mixed drill' : '$section drill',
          questions: questions,
          practice: true,
          progress: progress,
          recordId: section == null ? 'drill-mixed' : 'drill-$section',
        ),
      ),
    );
  }
}

class _HeroStat extends StatelessWidget {
  const _HeroStat({required this.value, required this.label});

  final String value;
  final String label;

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 12, horizontal: 8),
        decoration: BoxDecoration(
          color: Colors.white.withValues(alpha: 0.12),
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: Colors.white.withValues(alpha: 0.14)),
        ),
        child: Column(
          children: [
            Text(
              value,
              style: Theme.of(context).textTheme.titleLarge?.copyWith(
                    color: Colors.white,
                  ),
            ),
            const SizedBox(height: 2),
            Text(
              label,
              style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                    color: const Color(0xFFD5E7EC),
                    fontSize: 12,
                  ),
            ),
          ],
        ),
      ),
    );
  }
}

class _PaperCard extends StatelessWidget {
  const _PaperCard({
    required this.exam,
    required this.stats,
    required this.accent,
    required this.icon,
    required this.onTap,
  });

  final ExamPaper exam;
  final ExamStats stats;
  final Color accent;
  final IconData icon;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final text = Theme.of(context).textTheme;
    final best = stats.bestTotal == 0
        ? 'Not tried yet'
        : 'Best ${(stats.bestRate * 100).round()}%';
    return Container(
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(24),
        boxShadow: AppDecor.card,
      ),
      child: Material(
      color: AppColors.card,
      borderRadius: BorderRadius.circular(24),
      child: InkWell(
        borderRadius: BorderRadius.circular(24),
        onTap: onTap,
        child: Padding(
            padding: const EdgeInsets.all(16),
            child: Row(
              children: [
                Container(
                  width: 52,
                  height: 52,
                  decoration: BoxDecoration(
                    color: accent.withValues(alpha: 0.12),
                    borderRadius: BorderRadius.circular(16),
                  ),
                  child: Icon(icon, color: accent),
                ),
                const SizedBox(width: 14),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(exam.title, style: text.titleMedium),
                      const SizedBox(height: 4),
                      Text(
                        '${exam.questions.length} questions · ${exam.minutes} min',
                        style: text.bodyMedium,
                      ),
                      const SizedBox(height: 8),
                      Row(
                        children: [
                          Container(
                            width: 7,
                            height: 7,
                            decoration: BoxDecoration(
                              color: accent,
                              shape: BoxShape.circle,
                            ),
                          ),
                          const SizedBox(width: 6),
                          Text(best, style: text.bodyMedium?.copyWith(color: AppColors.ink)),
                        ],
                      ),
                    ],
                  ),
                ),
                Container(
                  width: 36,
                  height: 36,
                  decoration: BoxDecoration(
                    color: AppColors.mist,
                    shape: BoxShape.circle,
                  ),
                  child: const Icon(
                    Icons.arrow_forward_rounded,
                    size: 18,
                    color: AppColors.forest,
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class _AboutTile extends StatelessWidget {
  const _AboutTile({required this.onTap});

  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(22),
        boxShadow: AppDecor.card,
      ),
      child: Material(
        color: AppColors.card,
        borderRadius: BorderRadius.circular(22),
        child: InkWell(
          borderRadius: BorderRadius.circular(22),
          onTap: onTap,
          child: Padding(
            padding: const EdgeInsets.all(16),
            child: Row(
              children: [
                Container(
                  width: 46,
                  height: 46,
                  decoration: BoxDecoration(
                    color: AppColors.rightWash,
                    borderRadius: BorderRadius.circular(14),
                  ),
                  child: const Icon(Icons.info_outline_rounded, color: AppColors.forest),
                ),
                const SizedBox(width: 14),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text('About', style: Theme.of(context).textTheme.titleMedium),
                      const SizedBox(height: 2),
                      Text(
                        AboutScreen.name,
                        style: Theme.of(context).textTheme.bodyMedium,
                      ),
                    ],
                  ),
                ),
                const Icon(Icons.chevron_right_rounded, color: AppColors.inkSoft),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class _DrillCard extends StatelessWidget {
  const _DrillCard({
    required this.label,
    required this.icon,
    required this.color,
    required this.onTap,
  });

  final String label;
  final IconData icon;
  final Color color;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(right: 12),
      child: Container(
        width: 168,
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(22),
          boxShadow: AppDecor.card,
        ),
        child: Material(
        color: AppColors.card,
        borderRadius: BorderRadius.circular(22),
        child: InkWell(
          borderRadius: BorderRadius.circular(22),
          onTap: onTap,
          child: Padding(
              padding: const EdgeInsets.all(14),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Container(
                    width: 36,
                    height: 36,
                    decoration: BoxDecoration(
                      color: color.withValues(alpha: 0.12),
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: Icon(icon, color: color, size: 20),
                  ),
                  const Spacer(),
                  Text(
                    label,
                    maxLines: 2,
                    overflow: TextOverflow.ellipsis,
                    style: Theme.of(context).textTheme.titleMedium,
                  ),
                  Text('10 questions', style: Theme.of(context).textTheme.bodyMedium),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
