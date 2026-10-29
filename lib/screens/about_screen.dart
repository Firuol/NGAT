import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:ngat_practice/theme/app_theme.dart';

class AboutScreen extends StatelessWidget {
  const AboutScreen({super.key});

  static const name = 'Firaol Tesfaye';
  static const phone = '+251963178122';

  @override
  Widget build(BuildContext context) {
    final text = Theme.of(context).textTheme;
    return Scaffold(
      appBar: AppBar(title: const Text('About')),
      body: ListView(
        padding: const EdgeInsets.fromLTRB(22, 8, 22, 28),
        children: [
          Center(
            child: Container(
              padding: const EdgeInsets.fromLTRB(16, 12, 18, 12),
              decoration: BoxDecoration(
                color: AppColors.card,
                borderRadius: BorderRadius.circular(22),
                boxShadow: AppDecor.card,
              ),
              child: Image.asset(
                'assets/logo.png',
                height: 88,
                fit: BoxFit.contain,
              ),
            ),
          ),
          const SizedBox(height: 22),
          Text('NGAT Practice', style: text.displaySmall, textAlign: TextAlign.center),
          const SizedBox(height: 8),
          Text(
            'A practice app for the National Graduate Admission Test, with worked answers for every question.',
            style: text.bodyLarge,
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 24),
          Text('Developer', style: text.titleLarge),
          const SizedBox(height: 12),
          _InfoCard(
            icon: Icons.person_rounded,
            label: 'Name',
            value: name,
          ),
          const SizedBox(height: 10),
          _InfoCard(
            icon: Icons.phone_rounded,
            label: 'Phone',
            value: phone,
            onTap: () async {
              await Clipboard.setData(const ClipboardData(text: phone));
              if (!context.mounted) return;
              ScaffoldMessenger.of(context).showSnackBar(
                const SnackBar(content: Text('Phone number copied')),
              );
            },
          ),
        ],
      ),
    );
  }
}

class _InfoCard extends StatelessWidget {
  const _InfoCard({
    required this.icon,
    required this.label,
    required this.value,
    this.onTap,
  });

  final IconData icon;
  final String label;
  final String value;
  final VoidCallback? onTap;

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(20),
        boxShadow: AppDecor.card,
      ),
      child: Material(
      color: AppColors.card,
      borderRadius: BorderRadius.circular(20),
      child: InkWell(
        borderRadius: BorderRadius.circular(20),
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
                  child: Icon(icon, color: AppColors.forest),
                ),
                const SizedBox(width: 14),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(label, style: Theme.of(context).textTheme.bodyMedium),
                      const SizedBox(height: 2),
                      Text(value, style: Theme.of(context).textTheme.titleMedium),
                    ],
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
