import 'dart:convert';

import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';

class ExamStats {
  const ExamStats({
    this.attempts = 0,
    this.bestCorrect = 0,
    this.bestTotal = 0,
    this.lastCorrect = 0,
    this.lastTotal = 0,
  });

  final int attempts;
  final int bestCorrect;
  final int bestTotal;
  final int lastCorrect;
  final int lastTotal;

  double get bestRate => bestTotal == 0 ? 0 : bestCorrect / bestTotal;

  ExamStats copyWith({
    int? attempts,
    int? bestCorrect,
    int? bestTotal,
    int? lastCorrect,
    int? lastTotal,
  }) {
    return ExamStats(
      attempts: attempts ?? this.attempts,
      bestCorrect: bestCorrect ?? this.bestCorrect,
      bestTotal: bestTotal ?? this.bestTotal,
      lastCorrect: lastCorrect ?? this.lastCorrect,
      lastTotal: lastTotal ?? this.lastTotal,
    );
  }

  Map<String, dynamic> toJson() => {
        'attempts': attempts,
        'bestCorrect': bestCorrect,
        'bestTotal': bestTotal,
        'lastCorrect': lastCorrect,
        'lastTotal': lastTotal,
      };

  factory ExamStats.fromJson(Map<String, dynamic> json) {
    return ExamStats(
      attempts: json['attempts'] as int? ?? 0,
      bestCorrect: json['bestCorrect'] as int? ?? 0,
      bestTotal: json['bestTotal'] as int? ?? 0,
      lastCorrect: json['lastCorrect'] as int? ?? 0,
      lastTotal: json['lastTotal'] as int? ?? 0,
    );
  }
}

class ProgressStore extends ChangeNotifier {
  ProgressStore(this._prefs);

  final SharedPreferences _prefs;
  static const _key = 'ngat_progress_v1';

  int lifetimeCorrect = 0;
  int lifetimeAnswered = 0;
  final Map<String, ExamStats> exams = {};

  factory ProgressStore.load(SharedPreferences prefs) {
    final store = ProgressStore(prefs);
    final raw = prefs.getString(_key);
    if (raw == null) return store;
    final json = jsonDecode(raw) as Map<String, dynamic>;
    store.lifetimeCorrect = json['lifetimeCorrect'] as int? ?? 0;
    store.lifetimeAnswered = json['lifetimeAnswered'] as int? ?? 0;
    final saved = json['exams'] as Map<String, dynamic>? ?? {};
    for (final entry in saved.entries) {
      store.exams[entry.key] =
          ExamStats.fromJson(entry.value as Map<String, dynamic>);
    }
    return store;
  }

  double get accuracy =>
      lifetimeAnswered == 0 ? 0 : lifetimeCorrect / lifetimeAnswered;

  ExamStats statsFor(String id) => exams[id] ?? const ExamStats();

  Future<void> record({
    required String examId,
    required int correct,
    required int total,
  }) async {
    final current = statsFor(examId);
    final better = current.bestTotal == 0 ||
        correct / total > current.bestCorrect / current.bestTotal;
    exams[examId] = current.copyWith(
      attempts: current.attempts + 1,
      bestCorrect: better ? correct : current.bestCorrect,
      bestTotal: better ? total : current.bestTotal,
      lastCorrect: correct,
      lastTotal: total,
    );
    lifetimeCorrect += correct;
    lifetimeAnswered += total;
    await _prefs.setString(
      _key,
      jsonEncode({
        'lifetimeCorrect': lifetimeCorrect,
        'lifetimeAnswered': lifetimeAnswered,
        'exams': exams.map((key, value) => MapEntry(key, value.toJson())),
      }),
    );
    notifyListeners();
  }
}
