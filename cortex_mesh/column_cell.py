class CorticalColumnCell:
    # Mô phỏng 1 Cột Vỏ Não gồm 16 vi nơ-ron xử lý đa chiều
    @staticmethod
    def process_signals(input_signals, synaptic_weights):
        activations = []
        for i in range(16):
            w = synaptic_weights[i] if i < len(synaptic_weights) else 0.5
            val = sum(s * w for s in input_signals) / max(len(input_signals), 1)
            activated = max(0.0, val)
            activations.append(round(activated, 4))
        
        column_output = round(sum(activations) / len(activations), 4)
        return {"column_output": column_output, "layer_activations": activations}
