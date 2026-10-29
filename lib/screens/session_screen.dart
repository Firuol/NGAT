import 'dart:async';

import 'package:flutter/material.dart';
import 'package:ngat_practice/models/bank.dart';
import 'package:ngat_practice/screens/result_screen.dart';
import 'package:ngat_practice/state/progress_store.dart';
import 'package:ngat_practice/theme/app_theme.dart';

class SessionScreen extends StatefulWidget {
  const SessionScreen({
    super.key,
    required this.title,
    required this.questions,
    required this.practice,
    required this.progress,
    required this.recordId,
    this.minutes,
    this.reviewAnswers,
  });

  final String title;
  final List<Question> questions;
  final bool practice;
  final int? minutes;
  final ProgressStore progress;
  final String recordId;
  final Map<int, int>? reviewAnswers;

  bool get reviewing => reviewAnswers != null;

  @override
  State<SessionScreen> createState() => _SessionScreenState();
}

class _SessionScreenState extends State<SessionScreen> {
  final _answers = <int, int>{};
  final _flagged = <int>{};
  int _index = 0;
  Timer? _ticker;
  Duration _left = Duration.zero;
  bool _finished = false;

  bool get _timed => widget.minutes != null && !widget.reviewing;

  @override
  void initState() {
    super.initState();
    if (widget.reviewAnswers != null) {
      _answers.addAll(widget.reviewAnswers!);
    }
    if (_timed) {
      _left = Duration(minutes: widget.minutes!);
      final ends = DateTime.now().add(_left);
      _ticker = Timer.periodic(const Duration(seconds: 1), (_) {
        final left = ends.difference(DateTime.now());
        if (!mounted || _finished) return;
        if (left <= Duration.zero) {
          _finish();
        } else {
          setState(() => _left = left);
        }
      });
    }
  }

  @override
  void dispose() {
    _ticker?.cancel();
    super.dispose();
  }

  Question get _question => widget.questions[_index];

  bool get _revealed =>
      widget.reviewing || (widget.practice && _answers.containsKey(_index));

  Future<void> _finish() async {
    if (_finished) return;
    _finished = true;
    _ticker?.cancel();
    final correct = widget.questions.asMap().entries.where((entry) {
      final choice = _answers[entry.key];
      return choice != null && entry.value.accepts(choice);
    }).length;
    if (!widget.reviewing) {
      await widget.progress.record(
        examId: widget.recordId,
        correct: correct,
        total: widget.questions.length,
      );
    }
    if (!mounted) return;
    Navigator.of(context).pushReplacement(
      MaterialPageRoute(
        builder: (_) => ResultScreen(
          title: widget.title,
          questions: widget.questions,
          answers: Map<int, int>.from(_answers),
          progress: widget.progress,
          recordId: widget.recordId,
        ),
      ),
    );
  }

  Future<void> _close() async {
    if (widget.reviewing || _answers.isEmpty) {
      Navigator.of(context).pop();
      return;
    }
    final leave = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Leave this paper?'),
        content: const Text('Your answers in this sitting will not be saved.'),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context, false),
            child: const Text('Stay'),
          ),
          TextButton(
            onPressed: () => Navigator.pop(context, true),
            child: const Text('Leave'),
          ),
        ],
      ),
    );
    if (leave == true && mounted) Navigator.of(context).pop();
  }

  void _choose(int choice) {
    if (widget.reviewing || (widget.practice && _answers.containsKey(_index))) {
      return;
    }
    setState(() => _answers[_index] = choice);
  }

  @override
  Widget build(BuildContext context) {
    final text = Theme.of(context).textTheme;
    final total = widget.questions.length;
    final clock = _timed ? _format(_left) : null;
    return PopScope(
      canPop: widget.reviewing || _answers.isEmpty,
      onPopInvokedWithResult: (didPop, _) {
        if (!didPop) _close();
      },
      child: Scaffold(
        appBar: AppBar(
          leading: IconButton(
            onPressed: _close,
            icon: const Icon(Icons.close_rounded),
          ),
          title: Text(widget.title),
          actions: [
            if (clock != null)
              Padding(
                padding: const EdgeInsets.only(right: 4),
                child: Center(
                  child: Container(
                    padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                    decoration: BoxDecoration(
                      color: _left.inSeconds < 60
                          ? AppColors.wrongWash
                          : AppColors.rightWash,
                      borderRadius: BorderRadius.circular(999),
                    ),
                    child: Text(
                      clock,
                      style: text.titleMedium?.copyWith(
                        color: _left.inSeconds < 60 ? AppColors.wrong : AppColors.forest,
                      ),
                    ),
                  ),
                ),
              ),
            IconButton(
              tooltip: 'Question list',
              onPressed: _openMap,
              icon: const Icon(Icons.grid_view_rounded),
            ),
          ],
        ),
        body: Column(
          children: [
            Padding(
              padding: const EdgeInsets.fromLTRB(22, 4, 22, 8),
              child: ClipRRect(
                borderRadius: BorderRadius.circular(99),
                child: LinearProgressIndicator(
                  value: total == 0 ? 0 : (_index + 1) / total,
                  minHeight: 6,
                  backgroundColor: AppColors.line,
                  color: AppColors.forest,
                ),
              ),
            ),
            Expanded(
              child: ListView(
                padding: const EdgeInsets.fromLTRB(22, 8, 22, 16),
                children: [
                  Wrap(
                    spacing: 8,
                    runSpacing: 8,
                    children: [
                      _Pill(
                        'Question ${_index + 1} of $total',
                        filled: true,
                      ),
                      _Pill(_question.section, filled: false),
                      _Pill(_question.topic, filled: false),
                    ],
                  ),
                  if (_question.passage != null) ...[
                    const SizedBox(height: 14),
                    Container(
                      constraints: const BoxConstraints(maxHeight: 210),
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        color: AppColors.card,
                        borderRadius: BorderRadius.circular(20),
                        boxShadow: AppDecor.card,
                      ),
                      child: SingleChildScrollView(
                        child: Text(
                          _question.passage!,
                          style: text.bodyMedium?.copyWith(color: AppColors.ink),
                        ),
                      ),
                    ),
                  ],
                  const SizedBox(height: 14),
                  Container(
                    width: double.infinity,
                    padding: const EdgeInsets.all(18),
                    decoration: BoxDecoration(
                      color: AppColors.card,
                      borderRadius: BorderRadius.circular(22),
                      boxShadow: AppDecor.card,
                    ),
                    child: Text(_question.stem, style: text.bodyLarge),
                  ),
                  const SizedBox(height: 16),
                  for (var i = 0; i < _question.choices.length; i++) ...[
                    _ChoiceTile(
                      letter: String.fromCharCode(65 + i),
                      text: _question.choices[i],
                      selected: _answers[_index] == i,
                      revealed: _revealed,
                      correct: _question.accepts(i),
                      isKey: i == _question.answer,
                      onTap: () => _choose(i),
                    ),
                    const SizedBox(height: 8),
                  ],
                  if (_revealed) ...[
                    const SizedBox(height: 8),
                    _Explanation(question: _question, picked: _answers[_index]),
                  ],
                ],
              ),
            ),
            _BottomBar(
              onPrevious: _index == 0 ? null : () => setState(() => _index -= 1),
              onFlag: widget.reviewing
                  ? null
                  : () => setState(() {
                        if (!_flagged.add(_index)) _flagged.remove(_index);
                      }),
              flagged: _flagged.contains(_index),
              onNext: () {
                if (_index == total - 1) {
                  if (widget.reviewing) {
                    Navigator.of(context).pop();
                  } else {
                    _finish();
                  }
                } else {
                  setState(() => _index += 1);
                }
              },
              nextLabel: _index == total - 1
                  ? (widget.reviewing ? 'Done' : 'Finish')
                  : 'Next',
            ),
          ],
        ),
      ),
    );
  }

  void _openMap() {
    showModalBottomSheet<void>(
      context: context,
      backgroundColor: AppColors.card,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
      ),
      builder: (context) {
        return Padding(
          padding: const EdgeInsets.fromLTRB(20, 16, 20, 28),
          child: Wrap(
            spacing: 8,
            runSpacing: 8,
            children: [
              for (var i = 0; i < widget.questions.length; i++)
                InkWell(
                  onTap: () {
                    setState(() => _index = i);
                    Navigator.pop(context);
                  },
                  borderRadius: BorderRadius.circular(12),
                  child: Container(
                    width: 44,
                    height: 44,
                    alignment: Alignment.center,
                    decoration: BoxDecoration(
                      color: i == _index
                          ? AppColors.forest
                          : _answers.containsKey(i)
                              ? AppColors.rightWash
                              : AppColors.mist,
                      borderRadius: BorderRadius.circular(12),
                      border: Border.all(
                        color: _flagged.contains(i) ? AppColors.gold : AppColors.line,
                        width: _flagged.contains(i) ? 2 : 1,
                      ),
                    ),
                    child: Text(
                      '${i + 1}',
                      style: TextStyle(
                        color: i == _index ? Colors.white : AppColors.ink,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ),
                ),
            ],
          ),
        );
      },
    );
  }

  String _format(Duration duration) {
    final minutes = duration.inMinutes.remainder(60).toString().padLeft(2, '0');
    final seconds = duration.inSeconds.remainder(60).toString().padLeft(2, '0');
    final hours = duration.inHours;
    if (hours > 0) return '$hours:$minutes:$seconds';
    return '$minutes:$seconds';
  }
}

class _Pill extends StatelessWidget {
  const _Pill(this.label, {required this.filled});

  final String label;
  final bool filled;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
      decoration: BoxDecoration(
        color: filled ? AppColors.forest : AppColors.card,
        borderRadius: BorderRadius.circular(999),
        boxShadow: filled ? null : AppDecor.card,
      ),
      child: Text(
        label,
        style: Theme.of(context).textTheme.labelLarge?.copyWith(
              color: filled ? Colors.white : AppColors.forest,
            ),
      ),
    );
  }
}

class _ChoiceTile extends StatelessWidget {
  const _ChoiceTile({
    required this.letter,
    required this.text,
    required this.selected,
    required this.revealed,
    required this.correct,
    required this.isKey,
    required this.onTap,
  });

  final String letter;
  final String text;
  final bool selected;
  final bool revealed;
  final bool correct;
  final bool isKey;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    Color background = AppColors.card;
    Color border = Colors.transparent;
    Color badge = AppColors.mist;
    Color badgeText = AppColors.ink;
    if (!revealed && selected) {
      background = AppColors.forestDeep;
      border = AppColors.forestDeep;
      badge = const Color(0xFF2F6E80);
      badgeText = Colors.white;
    } else if (revealed && (isKey || (selected && correct))) {
      background = AppColors.rightWash;
      border = AppColors.forest;
      badge = AppColors.forest;
      badgeText = Colors.white;
    } else if (revealed && selected && !correct) {
      background = AppColors.wrongWash;
      border = AppColors.wrong;
      badge = AppColors.wrong;
      badgeText = Colors.white;
    }
    final textColor = !revealed && selected ? Colors.white : AppColors.ink;
    return Material(
      color: background,
      borderRadius: BorderRadius.circular(18),
      child: InkWell(
        borderRadius: BorderRadius.circular(18),
        onTap: onTap,
        child: Container(
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(18),
            border: Border.all(color: border),
            boxShadow: revealed || selected ? null : AppDecor.card,
          ),
          child: Row(
            children: [
              Container(
                width: 32,
                height: 32,
                alignment: Alignment.center,
                decoration: BoxDecoration(color: badge, shape: BoxShape.circle),
                child: Text(
                  letter,
                  style: TextStyle(color: badgeText, fontWeight: FontWeight.w700),
                ),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: Text(
                  text,
                  style: Theme.of(context).textTheme.bodyLarge?.copyWith(color: textColor),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class _Explanation extends StatelessWidget {
  const _Explanation({required this.question, required this.picked});

  final Question question;
  final int? picked;

  @override
  Widget build(BuildContext context) {
    final right = picked != null && question.accepts(picked!);
    final missed = picked == null;
    final title = missed
        ? 'Not answered'
        : right
            ? 'Correct'
            : 'Not quite';
    final tone = right ? AppColors.forest : AppColors.wrong;
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: right ? AppColors.rightWash : AppColors.wrongWash,
        borderRadius: BorderRadius.circular(20),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(
                right ? Icons.check_circle_rounded : Icons.cancel_rounded,
                color: tone,
                size: 20,
              ),
              const SizedBox(width: 8),
              Text(title, style: Theme.of(context).textTheme.titleMedium?.copyWith(color: tone)),
            ],
          ),
          const SizedBox(height: 8),
          Text(
            'Answer ${String.fromCharCode(65 + question.answer)}',
            style: Theme.of(context).textTheme.labelLarge?.copyWith(color: AppColors.forest),
          ),
          const SizedBox(height: 8),
          Text(question.explanation, style: Theme.of(context).textTheme.bodyLarge),
        ],
      ),
    );
  }
}

class _BottomBar extends StatelessWidget {
  const _BottomBar({
    required this.onPrevious,
    required this.onFlag,
    required this.flagged,
    required this.onNext,
    required this.nextLabel,
  });

  final VoidCallback? onPrevious;
  final VoidCallback? onFlag;
  final bool flagged;
  final VoidCallback onNext;
  final String nextLabel;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(16, 10, 16, 16),
      decoration: const BoxDecoration(
        color: AppColors.mist,
      ),
      child: SafeArea(
        top: false,
        child: Row(
          children: [
            IconButton(
              onPressed: onPrevious,
              icon: const Icon(Icons.arrow_back_rounded),
            ),
            if (onFlag != null)
              IconButton(
                onPressed: onFlag,
                icon: Icon(
                  flagged ? Icons.bookmark_rounded : Icons.bookmark_border_rounded,
                  color: flagged ? AppColors.gold : AppColors.ink,
                ),
              ),
            const Spacer(),
            FilledButton(
              style: FilledButton.styleFrom(
                backgroundColor: AppColors.forest,
                minimumSize: const Size(120, 48),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(14),
                ),
              ),
              onPressed: onNext,
              child: Text(nextLabel),
            ),
          ],
        ),
      ),
    );
  }
}
