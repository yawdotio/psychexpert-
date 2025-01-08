from experta import *

# Define Facts
class MoodStressFact(Fact):
    """Defines the structure of inputs"""
    mood = Field(str, mandatory=True)
    sleep = Field(int, mandatory=True)
    activity = Field(int, default=0)
    major_event = Field(bool, default=False)

# Define the Knowledge Engine
class MoodStressEngine(KnowledgeEngine):

    @Rule(MoodStressFact(mood="sad", sleep=P(lambda x: x < 4)))
    def high_stress_low_mood(self):
        self.declare(Fact(stress="High", mood_state="Low"))

    @Rule(MoodStressFact(mood="happy", sleep=P(lambda x: x > 6)))
    def low_stress_happy(self):
        self.declare(Fact(stress="Low", mood_state="Happy"))

    @Rule(MoodStressFact(mood="anxious", major_event=True))
    def high_stress_anxious(self):
        self.declare(Fact(stress="High", mood_state="Anxious"))


def main():# Collect Inputs
    mood_input = input("How do you feel (e.g., happy, sad, anxious)? ").strip().lower()
    sleep_input = int(input("How many hours did you sleep last night? "))
    activity_input = int(input("How many minutes did you exercise today? "))
    major_event_input = input("Did you have a major event today (yes/no)? ").strip().lower() == "yes"

    # Initialize and Run the Engine
    engine = MoodStressEngine()
    engine.reset()
    engine.declare(MoodStressFact(mood=mood_input, sleep=sleep_input, activity=activity_input, major_event=major_event_input))
    engine.run()

    # Print Results
    for fact in engine.facts.values():
        if fact.get("stress"):
            print(f"Stress Level: {fact['stress']}")
        if fact.get("mood_state"):
            print(f"Mood: {fact['mood_state']}")

if __name__ == "__main__":
    main()