import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:ngat_practice/main.dart';
import 'package:ngat_practice/models/bank.dart';
import 'package:ngat_practice/state/progress_store.dart';
import 'package:shared_preferences/shared_preferences.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  test('question bank has a valid answer for every item', () {
    final raw = File('assets/questions/bank.json').readAsStringSync();
    final bank = QuestionBank.fromJson(jsonDecode(raw) as Map<String, dynamic>);
    expect(bank.exams, isNotEmpty);
    final ids = <String>{};
    for (final exam in bank.exams) {
      expect(exam.questions, isNotEmpty);
      for (final question in exam.questions) {
        expect(ids.add(question.id), isTrue, reason: question.id);
        expect(question.answer, inInclusiveRange(0, question.choices.length - 1));
        expect(question.explanation.trim(), isNotEmpty);
        for (final extra in question.alsoAccept) {
          expect(extra, inInclusiveRange(0, question.choices.length - 1));
        }
      }
    }
    expect(bank.all.length, greaterThan(100));
  });

  testWidgets('home shows the three papers', (tester) async {
    GoogleFonts.config.allowRuntimeFetching = false;
    SharedPreferences.setMockInitialValues({});
    await tester.binding.setSurfaceSize(const Size(420, 900));
    addTearDown(() => tester.binding.setSurfaceSize(null));
    await tester.pumpWidget(const _LoadedApp());
    await tester.pumpAndSettle();
    expect(find.text('Train for exam day.'), findsOneWidget);
    expect(find.text('NGAT Set A'), findsOneWidget);
    await tester.scrollUntilVisible(find.text('GAT Sample Paper'), 400);
    expect(find.text('NGAT Set B'), findsOneWidget);
    expect(find.text('GAT Sample Paper'), findsOneWidget);

    await tester.tap(find.text('NGAT Set A'));
    await tester.pumpAndSettle();
    expect(find.text('Practice'), findsOneWidget);
    await tester.tap(find.text('Practice'));
    await tester.pumpAndSettle();
    expect(find.textContaining('Question 1 of'), findsOneWidget);
    await tester.tap(find.text('damage'));
    await tester.pumpAndSettle();
    expect(find.text('Correct'), findsOneWidget);
    expect(find.textContaining('opposite of unify'), findsOneWidget);
  });
}

class _LoadedApp extends StatelessWidget {
  const _LoadedApp();

  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
      future: _boot(),
      builder: (context, snapshot) {
        if (!snapshot.hasData) return const SizedBox.shrink();
        final data = snapshot.data!;
        return NgatApp(bank: data.$1, progress: data.$2);
      },
    );
  }
}

Future<(QuestionBank, ProgressStore)> _boot() async {
  final raw = File('assets/questions/bank.json').readAsStringSync();
  final bank = QuestionBank.fromJson(jsonDecode(raw) as Map<String, dynamic>);
  final prefs = await SharedPreferences.getInstance();
  return (bank, ProgressStore.load(prefs));
}
