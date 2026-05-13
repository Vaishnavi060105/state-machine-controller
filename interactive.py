class StateMachineController:

    def __init__(self):

        self.state = "START"

        self.allowed_transitions = {
            "START": ["TECHNICAL"],
            "TECHNICAL": ["FOLLOW-UP"],
            "FOLLOW-UP": ["END"],
            "END": []
        }

    def transition(self, new_state):

        if new_state in self.allowed_transitions[self.state]:

            print(f"✅ {self.state} → {new_state}")

            self.state = new_state

        else:

            print(f"❌ Invalid Transition: {self.state} → {new_state}")



controller = StateMachineController()

while True:

    print(f"\nCurrent State: {controller.state}")

    next_state = input("Enter next state: ").upper()

    controller.transition(next_state)

    if controller.state == "END":
        print("\nConversation Finished")
        break