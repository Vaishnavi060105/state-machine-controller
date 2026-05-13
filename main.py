class StateMachineController:

    def __init__(self):

        self.state = "START"

        self.allowed_transitions = {
            "START": ["TECHNICAL"],
            "TECHNICAL": ["FOLLOW-UP"],
            "FOLLOW-UP": ["END"],
            "END": []
        }

    def get_current_state(self):
        return self.state

    def transition(self, new_state):

        print("\n---------------------------")

        print(f"Current State: {self.state}")
        print(f"Requested State: {new_state}")

        if new_state in self.allowed_transitions[self.state]:

            self.state = new_state

            print("✅ Transition Successful")
            print(f"New State: {self.state}")

        else:

            print("❌ Invalid Transition")

            print(
                f"Allowed States: "
                f"{self.allowed_transitions[self.state]}"
            )


# Driver Code
controller = StateMachineController()

controller.transition("TECHNICAL")
controller.transition("FOLLOW-UP")
controller.transition("END")

# Invalid transition
controller.transition("START")