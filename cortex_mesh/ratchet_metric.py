class UpwardRatchetGovernor:
    # CƠ CHẾ ĐƯỜNG CHÉO TĂNG TRƯỞNG: Chỉ số IQ chỉ được phép đi lên, không bao giờ tụt lùi
    @staticmethod
    def calculate_upward_iq(past_iq, new_signals_count, peers_count):
        delta_iq = (new_signals_count * 0.05) + (peers_count * 0.02)
        accumulated_iq = round(past_iq + max(0.01, delta_iq), 4)
        return accumulated_iq
