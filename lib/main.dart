import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:ngat_practice/models/bank.dart';
import 'package:ngat_practice/screens/home_screen.dart';
import 'package:ngat_practice/state/progress_store.dart';
import 'package:ngat_practice/theme/app_theme.dart';
import 'package:shared_preferences/shared_preferences.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  final raw = await rootBundle.loadString('assets/questions/bank.json');
  final bank = QuestionBank.fromJson(jsonDecode(raw) as Map<String, dynamic>);
  final prefs = await SharedPreferences.getInstance();
  final progress = ProgressStore.load(prefs);
  runApp(NgatApp(bank: bank, progress: progress));
}

class NgatApp extends StatelessWidget {
  const NgatApp({super.key, required this.bank, required this.progress});

  final QuestionBank bank;
  final ProgressStore progress;

  @override
  Widget build(BuildContext context) {
    return ListenableBuilder(
      listenable: progress,
      builder: (context, _) {
        return MaterialApp(
          title: 'NGAT Practice',
          debugShowCheckedModeBanner: false,
          theme: AppTheme.light(),
          home: HomeScreen(bank: bank, progress: progress),
        );
      },
    );
  }
}
