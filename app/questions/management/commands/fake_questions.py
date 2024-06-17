from django.core.management.base import BaseCommand

from ...models import Choice, Question


class Command(BaseCommand):
    help = "Populates the database with questions and choices"

    def handle(self, *args, **kwargs):
        questions_data = [
            {
                "text": "What is the capital of France?",
                "choices": [
                    ("Paris", True),
                    ("London", False),
                    ("Berlin", False),
                    ("Madrid", False),
                ],
            },
            {
                "text": "What is the largest planet in our Solar System?",
                "choices": [
                    ("Earth", False),
                    ("Jupiter", True),
                    ("Mars", False),
                    ("Venus", False),
                ],
            },
            {
                "text": "What is the chemical symbol for water?",
                "choices": [
                    ("H2O", True),
                    ("O2", False),
                    ("CO2", False),
                    ("HO", False),
                ],
            },
            {
                "text": "What year did World War I begin?",
                "choices": [
                    ("1914", True),
                    ("1918", False),
                    ("1939", False),
                    ("1945", False),
                ],
            },
            {
                "text": "Who wrote 'Romeo and Juliet'?",
                "choices": [
                    ("William Shakespeare", True),
                    ("Charles Dickens", False),
                    ("Jane Austen", False),
                    ("Mark Twain", False),
                ],
            },
            {
                "text": "What is the smallest country in the world?",
                "choices": [
                    ("Vatican City", True),
                    ("Monaco", False),
                    ("Nauru", False),
                    ("San Marino", False),
                ],
            },
            {
                "text": "What is the largest ocean on Earth?",
                "choices": [
                    ("Atlantic Ocean", False),
                    ("Indian Ocean", False),
                    ("Arctic Ocean", False),
                    ("Pacific Ocean", True),
                ],
            },
            {
                "text": "What is the capital of Japan?",
                "choices": [
                    ("Kyoto", False),
                    ("Osaka", False),
                    ("Tokyo", True),
                    ("Hiroshima", False),
                ],
            },
            {
                "text": "What year did the Titanic sink?",
                "choices": [
                    ("1910", False),
                    ("1912", True),
                    ("1914", False),
                    ("1916", False),
                ],
            },
            {
                "text": "What is the chemical symbol for gold?",
                "choices": [("Au", True), ("Ag", False), ("Pb", False), ("Pt", False)],
            },
            {
                "text": "Which planet is known as the Red Planet?",
                "choices": [
                    ("Earth", False),
                    ("Mars", True),
                    ("Jupiter", False),
                    ("Saturn", False),
                ],
            },
            {
                "text": "What is the longest river in the world?",
                "choices": [
                    ("Nile River", True),
                    ("Amazon River", False),
                    ("Yangtze River", False),
                    ("Mississippi River", False),
                ],
            },
            {
                "text": "What is the hardest natural substance on Earth?",
                "choices": [
                    ("Gold", False),
                    ("Iron", False),
                    ("Diamond", True),
                    ("Platinum", False),
                ],
            },
            {
                "text": "Who painted the Mona Lisa?",
                "choices": [
                    ("Vincent van Gogh", False),
                    ("Pablo Picasso", False),
                    ("Leonardo da Vinci", True),
                    ("Claude Monet", False),
                ],
            },
            {
                "text": "What is the capital of Australia?",
                "choices": [
                    ("Sydney", False),
                    ("Melbourne", False),
                    ("Canberra", True),
                    ("Perth", False),
                ],
            },
            {
                "text": "Which element has the atomic number 1?",
                "choices": [
                    ("Oxygen", False),
                    ("Helium", False),
                    ("Hydrogen", True),
                    ("Carbon", False),
                ],
            },
            {
                "text": "What is the tallest mountain in the world?",
                "choices": [
                    ("K2", False),
                    ("Mount Everest", True),
                    ("Kangchenjunga", False),
                    ("Lhotse", False),
                ],
            },
            {
                "text": "What is the capital of Canada?",
                "choices": [
                    ("Toronto", False),
                    ("Vancouver", False),
                    ("Ottawa", True),
                    ("Montreal", False),
                ],
            },
            {
                "text": "Who discovered penicillin?",
                "choices": [
                    ("Marie Curie", False),
                    ("Isaac Newton", False),
                    ("Alexander Fleming", True),
                    ("Louis Pasteur", False),
                ],
            },
            {
                "text": "What is the most widely spoken language in the world?",
                "choices": [
                    ("English", False),
                    ("Spanish", False),
                    ("Chinese", True),
                    ("Hindi", False),
                ],
            },
            {
                "text": "What is the smallest bone in the human body?",
                "choices": [
                    ("Stapes", True),
                    ("Femur", False),
                    ("Ulna", False),
                    ("Humerus", False),
                ],
            },
            {
                "text": "What is the currency of Japan?",
                "choices": [
                    ("Yuan", False),
                    ("Won", False),
                    ("Yen", True),
                    ("Ringgit", False),
                ],
            },
            {
                "text": "Who was the first President of the United States?",
                "choices": [
                    ("Abraham Lincoln", False),
                    ("George Washington", True),
                    ("Thomas Jefferson", False),
                    ("John Adams", False),
                ],
            },
            {
                "text": "What is the largest desert in the world?",
                "choices": [
                    ("Sahara Desert", True),
                    ("Arabian Desert", False),
                    ("Gobi Desert", False),
                    ("Kalahari Desert", False),
                ],
            },
            {
                "text": "Which planet is closest to the Sun?",
                "choices": [
                    ("Venus", False),
                    ("Earth", False),
                    ("Mercury", True),
                    ("Mars", False),
                ],
            },
            {
                "text": "Who wrote '1984'?",
                "choices": [
                    ("Aldous Huxley", False),
                    ("George Orwell", True),
                    ("Ray Bradbury", False),
                    ("J.D. Salinger", False),
                ],
            },
            {
                "text": "What is the capital of Italy?",
                "choices": [
                    ("Venice", False),
                    ("Milan", False),
                    ("Rome", True),
                    ("Florence", False),
                ],
            },
            {
                "text": "What is the largest mammal in the world?",
                "choices": [
                    ("Elephant", False),
                    ("Blue Whale", True),
                    ("Giraffe", False),
                    ("Great White Shark", False),
                ],
            },
            {
                "text": "What is the capital of Russia?",
                "choices": [
                    ("Saint Petersburg", False),
                    ("Moscow", True),
                    ("Novosibirsk", False),
                    ("Yekaterinburg", False),
                ],
            },
            {
                "text": "Which country is known as the Land of the Rising Sun?",
                "choices": [
                    ("China", False),
                    ("South Korea", False),
                    ("Japan", True),
                    ("Thailand", False),
                ],
            },
            {
                "text": "What is the chemical symbol for oxygen?",
                "choices": [("O", True), ("O2", False), ("Ox", False), ("Og", False)],
            },
            {
                "text": "What year did the Berlin Wall fall?",
                "choices": [
                    ("1985", False),
                    ("1987", False),
                    ("1989", True),
                    ("1991", False),
                ],
            },
            {
                "text": "Which country has the most volcanoes?",
                "choices": [
                    ("Japan", False),
                    ("Indonesia", True),
                    ("United States", False),
                    ("Russia", False),
                ],
            },
            {
                "text": "Who was the first man to step on the moon?",
                "choices": [
                    ("Buzz Aldrin", False),
                    ("Yuri Gagarin", False),
                    ("Neil Armstrong", True),
                    ("Michael Collins", False),
                ],
            },
            {
                "text": "What is the capital of Egypt?",
                "choices": [
                    ("Alexandria", False),
                    ("Cairo", True),
                    ("Giza", False),
                    ("Luxor", False),
                ],
            },
            {
                "text": "What is the primary ingredient in guacamole?",
                "choices": [
                    ("Tomato", False),
                    ("Onion", False),
                    ("Avocado", True),
                    ("Pepper", False),
                ],
            },
            {
                "text": "What year did the United States declare independence?",
                "choices": [
                    ("1775", False),
                    ("1776", True),
                    ("1781", False),
                    ("1783", False),
                ],
            },
            {
                "text": "What is the most abundant gas in Earth's atmosphere?",
                "choices": [
                    ("Oxygen", False),
                    ("Nitrogen", True),
                    ("Carbon Dioxide", False),
                    ("Argon", False),
                ],
            },
            {
                "text": "Who wrote 'To Kill a Mockingbird'?",
                "choices": [
                    ("Harper Lee", True),
                    ("Mark Twain", False),
                    ("Ernest Hemingway", False),
                    ("F. Scott Fitzgerald", False),
                ],
            },
            {
                "text": "What is the name of the longest river in South America?",
                "choices": [
                    ("Amazon River", True),
                    ("Nile River", False),
                    ("Mississippi River", False),
                    ("Yangtze River", False),
                ],
            },
            {
                "text": "What is the capital of Germany?",
                "choices": [
                    ("Munich", False),
                    ("Frankfurt", False),
                    ("Berlin", True),
                    ("Hamburg", False),
                ],
            },
            {
                "text": "What is the chemical formula for table salt?",
                "choices": [
                    ("NaCl", True),
                    ("KCl", False),
                    ("NaOH", False),
                    ("H2O", False),
                ],
            },
            {
                "text": "Who painted the ceiling of the Sistine Chapel?",
                "choices": [
                    ("Leonardo da Vinci", False),
                    ("Raphael", False),
                    ("Michelangelo", True),
                    ("Donatello", False),
                ],
            },
            {
                "text": "Which planet is known for its rings?",
                "choices": [
                    ("Mars", False),
                    ("Jupiter", False),
                    ("Saturn", True),
                    ("Neptune", False),
                ],
            },
            {
                "text": "What is the hardest rock?",
                "choices": [
                    ("Marble", False),
                    ("Granite", False),
                    ("Diamond", True),
                    ("Quartz", False),
                ],
            },
            {
                "text": "What is the capital of Spain?",
                "choices": [
                    ("Barcelona", False),
                    ("Madrid", True),
                    ("Seville", False),
                    ("Valencia", False),
                ],
            },
            {
                "text": "Who is the author of 'Harry Potter' series?",
                "choices": [
                    ("J.R.R. Tolkien", False),
                    ("C.S. Lewis", False),
                    ("J.K. Rowling", True),
                    ("George R.R. Martin", False),
                ],
            },
            {
                "text": "What is the freezing point of water?",
                "choices": [
                    ("0°C", True),
                    ("32°C", False),
                    ("100°C", False),
                    ("-1°C", False),
                ],
            },
            {
                "text": "Which country is known as the Land Down Under?",
                "choices": [
                    ("New Zealand", False),
                    ("Australia", True),
                    ("South Africa", False),
                    ("Brazil", False),
                ],
            },
            {
                "text": "What year did World War II end?",
                "choices": [
                    ("1943", False),
                    ("1945", True),
                    ("1947", False),
                    ("1950", False),
                ],
            },
        ]

        for q_data in questions_data:
            question = Question.objects.create(text=q_data["text"])
            for choice_text, is_correct in q_data["choices"]:
                Choice.objects.create(
                    question=question, text=choice_text, is_correct=is_correct
                )

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully populated the database with questions and choices"
            )
        )
