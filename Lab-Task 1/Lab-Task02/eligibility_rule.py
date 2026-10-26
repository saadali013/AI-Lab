class TemperatureController:
    def __init__(self):
        self.previous_mode = None

    def determine_mode(self, temperature, occupied):
        # Occupancy has priority
        if not occupied:
            target_mode = "OFF"
        elif temperature < 18:
            target_mode = "HEAT"
        elif temperature > 26:
            target_mode = "COOL"
        else:
            target_mode = "OFF"

        # Check whether the mode has changed
        send_command = target_mode != self.previous_mode

        # Save the current target mode
        self.previous_mode = target_mode

        return target_mode, send_command


# Create controller
controller = TemperatureController()

# Test cases
test_cases = [
    {
        "name": "Heating mode",
        "temperature": 16,
        "occupied": True
    },
    {
        "name": "Repeated heating mode",
        "temperature": 16,
        "occupied": True
    },
    {
        "name": "Lower boundary",
        "temperature": 18,
        "occupied": True
    },
    {
        "name": "Upper boundary",
        "temperature": 26,
        "occupied": True
    },
    {
        "name": "Cooling mode",
        "temperature": 30,
        "occupied": True
    },
    {
        "name": "Repeated cooling mode",
        "temperature": 30,
        "occupied": True
    },
    {
        "name": "Empty room",
        "temperature": 16,
        "occupied": False
    }
]

# Run tests
print("Temperature Control System")
print("-" * 85)
print(
    f"{'Previous Mode':<15}"
    f"{'Percept':<25}"
    f"{'Target':<12}"
    f"{'Outcome'}"
)
print("-" * 85)

for case in test_cases:
    previous_mode = controller.previous_mode

    percept = (
        f"Temp={case['temperature']}, "
        f"Occupied={case['occupied']}"
    )

    target_mode, send_command = controller.determine_mode(
        case["temperature"],
        case["occupied"]
    )

    outcome = "SEND COMMAND" if send_command else "NO COMMAND"

    print(
        f"{str(previous_mode):<15}"
        f"{percept:<25}"
        f"{target_mode:<12}"
        f"{outcome}"
    )
