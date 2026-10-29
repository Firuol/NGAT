import 'package:flutter/material.dart';
import 'package:ngat_practice/models/bank.dart';
import 'package:ngat_practice/screens/session_screen.dart';
import 'package:ngat_practice/state/progress_store.dart';
import 'package:ngat_practice/theme/app_theme.dart';

class ResultScreen extends StatelessWidget {
  const ResultScreen({
    super.key,
    required this.title,
    required this.questions,
    required this.answers,
    required this.progress,
    required this.recordId,
  });

  final String title;
  final List<Question> questions;
  final Map<int, int> answers;
  final ProgressStore progress;
  final String recordId;

  int get correctCount => questions
      .asMap()
      .entries
      .where((entry) {
        final choice = answers[entry.key];
        return choice != null && entry.value.accepts(choice);
      })
      .length;

  @override
  Widget build(BuildContext context) {
    final text = Theme.of(context).textTheme;
    final correct = correctCount;
    final total = questions.length;
    final rate = total == 0 ? 0.0 : correct / total;
    final sections = <String, List<int>>{};
    for (var i = 0; i < questions.length; i++) {
      sections.putIfAbsent(questions[i].section, () => []).add(i);
    }

    return Scaffold(
      appBar: AppBar(title: const Text('Your result')),
      body: ListView(
        padding: const EdgeInsets.fromLTRB(22, 8, 22, 28),
        children: [
          Container(
            padding: const EdgeInsets.fromLTRB(22, 28, 22, 26),
            decoration: BoxDecoration(
              gradient: const LinearGradient(
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
                colors: [Color(0xFF2E6E80), AppColors.forestDeep],
              ),
              borderRadius: BorderRadius.circular(32),
              boxShadow: AppDecor.card,
            ),
            child: Column(
              children: [
                Text(
                  title,
                  style: text.bodyMedium?.copyWith(color: const Color(0xFFD5E7EC)),
                ),
                const SizedBox(height: 18),
                SizedBox(
                  width: 148,
                  height: 148,
                  child: Stack(
                    alignment: Alignment.center,
                    children: [
                      SizedBox(
                        width: 148,
                        height: 148,
                        child: CircularProgressIndicator(
                          value: rate,
                          strokeWidth: 12,
                          strokeCap: StrokeCap.round,
                          backgroundColor: Colors.white.withValues(alpha: 0.16),
                          color: AppColors.aqua,
                        ),
                      ),
                      Column(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Text(
                            '${(rate * 100).round()}%',
                            style: text.headlineMedium?.copyWith(color: Colors.white),
                          ),
                          Text(
                            '$correct of $total',
                            style: text.bodyMedium?.copyWith(color: const Color(0xFFD5E7EC)),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 22),
          Text('By section', style: text.titleLarge),
          const SizedBox(height: 12),
          for (final entry in sections.entries) ...[
            _SectionScore(
              name: entry.key,
              indexes: entry.value,
              questions: questions,
              answers: answers,
            ),
            const SizedBox(height: 10),
          ],
          const SizedBox(height: 18),
          FilledButton(
            style: FilledButton.styleFrom(
              backgroundColor: AppColors.forest,
              minimumSize: const Size.fromHeight(52),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(16),
              ),
            ),
            onPressed: () {
              Navigator.of(context).push(
                MaterialPageRoute(
                  builder: (_) => SessionScreen(
                    title: title,
                    questions: questions,
                    practice: false,
                    progress: progress,
                    recordId: recordId,
                    reviewAnswers: answers,
                  ),
                ),
              );
            },
            child: const Text('Review explanations'),
          ),
        ],
      ),
    );
  }
}

class _SectionScore extends StatelessWidget {
  const _SectionScore({
    required this.name,
    required this.indexes,
    required this.questions,
    required this.answers,
  });

  final String name;
  final List<int> indexes;
  final List<Question> questions;
  final Map<int, int> answers;

  @override
  Widget build(BuildContext context) {
    final correct = indexes.where((index) {
      final choice = answers[index];
      return choice != null && questions[index].accepts(choice);
    }).length;
    final rate = indexes.isEmpty ? 0.0 : correct / indexes.length;
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: AppColors.card,
        borderRadius: BorderRadius.circular(18),
        boxShadow: AppDecor.card,
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Expanded(
                child: Text(name, style: Theme.of(context).textTheme.titleMedium),
              ),
              Text('$correct / ${indexes.length}'),
            ],
          ),
          const SizedBox(height: 10),
          ClipRRect(
            borderRadius: BorderRadius.circular(99),
            child: LinearProgressIndicator(
              value: rate,
              minHeight: 8,
              backgroundColor: AppColors.line,
              color: AppColors.forest,
            ),
          ),
        ],
      ),
    );
  }
}
