class Question {
  const Question({
    required this.id,
    required this.section,
    required this.topic,
    required this.stem,
    required this.choices,
    required this.answer,
    required this.explanation,
    this.passage,
    this.alsoAccept = const [],
  });

  final String id;
  final String section;
  final String topic;
  final String stem;
  final List<String> choices;
  final int answer;
  final List<int> alsoAccept;
  final String explanation;
  final String? passage;

  bool accepts(int choice) => choice == answer || alsoAccept.contains(choice);

  factory Question.fromJson(Map<String, dynamic> json) {
    return Question(
      id: json['id'] as String,
      section: json['section'] as String,
      topic: json['topic'] as String,
      stem: json['stem'] as String,
      choices: (json['choices'] as List).cast<String>(),
      answer: json['answer'] as int,
      alsoAccept: (json['alsoAccept'] as List?)?.cast<int>() ?? const [],
      explanation: json['explanation'] as String,
      passage: json['passage'] as String?,
    );
  }
}

class ExamPaper {
  const ExamPaper({
    required this.id,
    required this.title,
    required this.summary,
    required this.source,
    required this.minutes,
    required this.questions,
  });

  final String id;
  final String title;
  final String summary;
  final String source;
  final int minutes;
  final List<Question> questions;

  Map<String, int> get sectionCounts {
    final counts = <String, int>{};
    for (final question in questions) {
      counts[question.section] = (counts[question.section] ?? 0) + 1;
    }
    return counts;
  }

  factory ExamPaper.fromJson(Map<String, dynamic> json) {
    return ExamPaper(
      id: json['id'] as String,
      title: json['title'] as String,
      summary: json['summary'] as String,
      source: json['source'] as String,
      minutes: json['minutes'] as int,
      questions: (json['questions'] as List)
          .map((item) => Question.fromJson(item as Map<String, dynamic>))
          .toList(),
    );
  }
}

class QuestionBank {
  const QuestionBank(this.exams);

  final List<ExamPaper> exams;

  List<Question> get all =>
      exams.expand((exam) => exam.questions).toList(growable: false);

  factory QuestionBank.fromJson(Map<String, dynamic> json) {
    return QuestionBank(
      (json['exams'] as List)
          .map((item) => ExamPaper.fromJson(item as Map<String, dynamic>))
          .toList(),
    );
  }
}
