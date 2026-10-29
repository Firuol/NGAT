import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:google_fonts/google_fonts.dart';

class AppColors {
  static const ink = Color(0xFF102126);
  static const inkSoft = Color(0xFF5C7076);
  static const forest = Color(0xFF235562);
  static const forestDeep = Color(0xFF14343D);
  static const mist = Color(0xFFF3F7F8);
  static const card = Color(0xFFFFFFFF);
  static const line = Color(0xFFE2EBED);
  static const gold = Color(0xFFE2A23A);
  static const wrong = Color(0xFFC44848);
  static const wrongWash = Color(0xFFFDECEC);
  static const rightWash = Color(0xFFE7F4F6);
  static const aqua = Color(0xFF7EC8D6);
}

class AppDecor {
  static List<BoxShadow> get card => const [
        BoxShadow(
          color: Color(0x14235562),
          blurRadius: 28,
          offset: Offset(0, 12),
        ),
      ];
}

class AppTheme {
  static ThemeData light() {
    final textTheme = TextTheme(
      displaySmall: GoogleFonts.plusJakartaSans(
        fontSize: 32,
        height: 1.12,
        fontWeight: FontWeight.w800,
        color: AppColors.ink,
        letterSpacing: -0.6,
      ),
      headlineMedium: GoogleFonts.plusJakartaSans(
        fontSize: 28,
        height: 1.15,
        fontWeight: FontWeight.w800,
        color: AppColors.ink,
        letterSpacing: -0.4,
      ),
      titleLarge: GoogleFonts.plusJakartaSans(
        fontSize: 20,
        fontWeight: FontWeight.w700,
        color: AppColors.ink,
        letterSpacing: -0.2,
      ),
      titleMedium: GoogleFonts.plusJakartaSans(
        fontSize: 16,
        fontWeight: FontWeight.w700,
        color: AppColors.ink,
      ),
      bodyLarge: GoogleFonts.plusJakartaSans(
        fontSize: 16,
        height: 1.45,
        fontWeight: FontWeight.w500,
        color: AppColors.ink,
      ),
      bodyMedium: GoogleFonts.plusJakartaSans(
        fontSize: 14,
        height: 1.4,
        fontWeight: FontWeight.w500,
        color: AppColors.inkSoft,
      ),
      labelLarge: GoogleFonts.plusJakartaSans(
        fontSize: 14,
        fontWeight: FontWeight.w700,
        letterSpacing: 0.1,
      ),
    );

    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.light,
      scaffoldBackgroundColor: AppColors.mist,
      colorScheme: const ColorScheme.light(
        primary: AppColors.forest,
        onPrimary: Colors.white,
        secondary: AppColors.gold,
        surface: AppColors.card,
        onSurface: AppColors.ink,
      ),
      textTheme: textTheme,
      appBarTheme: AppBarTheme(
        backgroundColor: AppColors.mist,
        foregroundColor: AppColors.ink,
        elevation: 0,
        scrolledUnderElevation: 0,
        centerTitle: false,
        systemOverlayStyle: SystemUiOverlayStyle.dark,
        titleTextStyle: textTheme.titleLarge,
      ),
      dividerColor: AppColors.line,
      filledButtonTheme: FilledButtonThemeData(
        style: FilledButton.styleFrom(
          backgroundColor: AppColors.forest,
          foregroundColor: Colors.white,
          textStyle: GoogleFonts.plusJakartaSans(
            fontWeight: FontWeight.w700,
            fontSize: 15,
          ),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(16),
          ),
        ),
      ),
    );
  }
}
