import 'package:flutter/material.dart';
import 'package:ngat_practice/models/bank.dart';
import 'package:ngat_practice/screens/session_screen.dart';
import 'package:ngat_practice/state/progress_store.dart';
import 'package:ngat_practice/theme/app_theme.dart';

class PaperScreen extends StatelessWidget {
  const PaperScreen({super.key, required this.exam, required this.progress});

  final ExamPaper exam;
  final ProgressStore progress;

  @override
  Widget build(BuildContext context) {
    final text = Theme.of(context).textTheme;
    final sections = exam.sectionCounts.entries.toList();
    final stats = progress.statsFor(exam.id);
    return Scaffold(
      appBar: AppBar(),
      body: ListView(
        padding: const EdgeInsets.fromLTRB(22, 0, 22, 28),
        children: [
          Text(exam.title, style: text.displaySmall),
          const SizedBox(height: 8),
          Text(exam.summary, style: text.bodyLarge),
          const SizedBox(height: 6),
          Text(exam.source, style: text.bodyMedium),
          if (stats.bestTotal > 0) ...[
            const SizedBox(height: 14),
            Text(
              'Best score ${(stats.bestRate * 100).round()}% · ${stats.attempts} attempt${stats.attempts == 1 ? '' : 's'}',
              style: text.titleMedium?.copyWith(color: AppColors.forest),
            ),
          ],
          const SizedBox(height: 20),
          _ModeCard(
            icon: Icons.lightbulb_outline_rounded,
            title: 'Practice',
            detail: 'See the explanation after each answer',
            filled: false,
            onTap: () => _open(context, exam.questions, practice: true),
          ),
          const SizedBox(height: 12),
          _ModeCard(
            icon: Icons.timer_outlined,
            title: 'Timed paper',
            detail: '${exam.minutes} minutes, then review what you missed',
            filled: true,
            onTap: () => _open(
              context,
              exam.questions,
              practice: false,
              minutes: exam.minutes,
            ),
          ),
          const SizedBox(height: 28),
          Text('Practice a section', style: text.titleLarge),
          const SizedBox(height: 12),
          for (final section in sections) ...[
            _SectionRow(
              name: section.key,
              count: section.value,
              icon: _iconFor(section.key),
              onTap: () {
                final questions = exam.questions
                    .where((question) => question.section == section.key)
                    .toList();
                _open(context, questions, practice: true, title: section.key);
              },
            ),
            const SizedBox(height: 10),
          ],
        ],
      ),
    );
  }

  IconData _iconFor(String section) {
    return switch (section) {
      'Verbal' => Icons.abc_rounded,
      'Quantitative' => Icons.calculate_rounded,
      'Logical' => Icons.hub_rounded,
      'Analytical' => Icons.account_tree_rounded,
      _ => Icons.notes_rounded,
    };
  }

  void _open(
    BuildContext context,
    List<Question> questions, {
    required bool practice,
    int? minutes,
    String? title,
  }) {
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (_) => SessionScreen(
          title: title ?? exam.title,
          questions: questions,
          practice: practice,
          minutes: minutes,
          progress: progress,
          recordId: exam.id,
        ),
      ),
    );
  }
}

class _ModeCard extends StatelessWidget {
  const _ModeCard({
    required this.icon,
    required this.title,
    required this.detail,
    required this.filled,
    required this.onTap,
  });

  final IconData icon;
  final String title;
  final String detail;
  final bool filled;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final foreground = filled ? Colors.white : AppColors.ink;
    return Container(
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(22),
        boxShadow: AppDecor.card,
      ),
      child: Material(
      color: filled ? Colors.transparent : AppColors.card,
      borderRadius: BorderRadius.circular(22),
      child: InkWell(
        borderRadius: BorderRadius.circular(22),
        onTap: onTap,
        child: Ink(
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(22),
            gradient: filled
                ? const LinearGradient(
                    colors: [Color(0xFF2E6E80), AppColors.forestDeep],
                  )
                : null,
            color: filled ? null : AppColors.card,
          ),
          child: Padding(
            padding: const EdgeInsets.all(18),
            child: Row(
              children: [
                Container(
                  width: 46,
                  height: 46,
                  decoration: BoxDecoration(
                    color: filled
                        ? Colors.white.withValues(alpha: 0.16)
                        : AppColors.rightWash,
                    borderRadius: BorderRadius.circular(14),
                  ),
                  child: Icon(
                    icon,
                    color: filled ? Colors.white : AppColors.forest,
                  ),
                ),
                const SizedBox(width: 14),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        title,
                        style: Theme.of(context).textTheme.titleLarge?.copyWith(
                              color: foreground,
                              fontSize: 18,
                            ),
                      ),
                      const SizedBox(height: 4),
                      Text(
                        detail,
                        style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                              color: filled
                                  ? const Color(0xFFD5E6EB)
                                  : AppColors.inkSoft,
                            ),
                      ),
                    ],
                  ),
                ),
                Icon(
                  Icons.arrow_forward_rounded,
                  color: filled ? Colors.white : AppColors.forest,
                ),
              ],
            ),
          ),
        ),
      ),
      ),
    );
  }
}

class _SectionRow extends StatelessWidget {
  const _SectionRow({
    required this.name,
    required this.count,
    required this.icon,
    required this.onTap,
  });

  final String name;
  final int count;
  final IconData icon;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(18),
        boxShadow: AppDecor.card,
      ),
      child: Material(
      color: AppColors.card,
      borderRadius: BorderRadius.circular(18),
      child: InkWell(
        borderRadius: BorderRadius.circular(18),
        onTap: onTap,
        child: Ink(
          decoration: const BoxDecoration(
            color: AppColors.card,
            borderRadius: BorderRadius.all(Radius.circular(18)),
          ),
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
            child: Row(
              children: [
                Container(
                  width: 40,
                  height: 40,
                  decoration: BoxDecoration(
                    color: AppColors.rightWash,
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: Icon(icon, color: AppColors.forest, size: 20),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: Text(name, style: Theme.of(context).textTheme.titleMedium),
                ),
                Text(
                  '$count',
                  style: Theme.of(context).textTheme.titleMedium?.copyWith(
                        color: AppColors.inkSoft,
                      ),
                ),
                const SizedBox(width: 4),
                const Icon(Icons.chevron_right_rounded, color: AppColors.inkSoft),
              ],
            ),
          ),
        ),
      ),
      ),
    );
  }
}
