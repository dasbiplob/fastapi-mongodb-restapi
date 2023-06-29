class Message:
    def __init__(self, session_id, energy_delivered, duration, session_cost):
        self.session_id = session_id
        self.energy_delivered = energy_delivered
        self.duration = duration
        self.session_cost = session_cost

    def to_dict(self):
        return {
            'session_id': self.session_id,
            'energy_delivered_in_kWh': self.energy_delivered,
            'duration_in_seconds': self.duration,
            'session_cost_in_cents': self.session_cost
        }
