from typing import Dict, List, Optional, Tuple, Union


Percept = Dict[str, Union[int, bool]]


class TemperatureController:
    def __init__(self) -> None:
        self.previous_target_mode: Optional[str] = None

    def process_percept(self, percept: Percept) -> Tuple[str, bool]:
        temperature = percept["temperature"]
        occupied = percept["occupied"]

        if not occupied:
            target_mode = "Off"
        elif temperature < 18:
            target_mode = "Heat"
        elif temperature > 26:
            target_mode = "Cool"
        else:
            target_mode = "Eco"

        should_send = target_mode != self.previous_target_mode
        self.previous_target_mode = target_mode
        return target_mode, should_send


def run_scenarios() -> List[Dict[str, object]]:
    scenarios = [
        ("cold room", {"temperature": 17, "occupied": True}),
        ("repeated cold room", {"temperature": 17, "occupied": True}),
        ("lower exact boundary", {"temperature": 18, "occupied": True}),
        ("upper exact boundary", {"temperature": 26, "occupied": True}),
        ("empty room at high temperature", {"temperature": 30, "occupied": False}),
    ]
    controller = TemperatureController()
    records = []

    for name, percept in scenarios:
        previous_mode = controller.previous_target_mode
        target_mode, should_send = controller.process_percept(percept)
        outcome = f"Command: {target_mode}" if should_send else "No command"
        records.append(
            {
                "scenario": name,
                "previous_mode": previous_mode,
                "percept": percept,
                "target": target_mode,
                "outcome": outcome,
            }
        )

    return records


if __name__ == "__main__":
    for record in run_scenarios():
        print(
            f"{record['scenario']}: previous={record['previous_mode']}, "
            f"percept={record['percept']}, target={record['target']}, "
            f"outcome={record['outcome']}"
        )