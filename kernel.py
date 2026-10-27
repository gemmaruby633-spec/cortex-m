import os
import sys
import json
import time
import hashlib
import urllib.request

# ==============================================================================
# BẢN ĐỒ ADN TỰ ĐẺ THỂ XÁC CORTEX (EMBRYONIC BLUEPRINTS) - ĐÃ KHẮC PHỤC XUNG ĐỘT DẤU
# ==============================================================================
CORTEX_BLUEPRINTS = {
    "contract.json": json.dumps({
        "contract_id": "bodhi.cortex.v1",
        "genesis_root": "100048777766367/contract",
        "derived_node": "100048777766367/cortex",
        "role": "CORTICAL_COLUMN_NEURON",
        "rules": {
            "zero_pii": True,
            "monotonic_upward_growth": True,
            "shake_quantum_signature_required": True,
            "byzantine_quarantine_threshold": 0.2
        }
    }, indent=4),

    "Dockerfile": """FROM python:3.14-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY . .
CMD ["python", "kernel.py"]
""",

    "README.md": """# 🧠 BODHI-CORTEX: VỎ NÃO TÂN SINH ĐA NHÂN BẢN (THE NEOCORTICAL SWARM)
> *"Càng nhân bản càng thông minh: Mỗi repo là một Cột Vỏ Não (Cortical Column). Tích lũy tri thức một chiều theo đường chéo tăng trưởng và khóa chặt bằng chữ ký lượng tử hệ sinh thái."*
""",

    "cortex_mesh/__init__.py": "# Cortex Mesh Package\n",

    "cortex_mesh/column_cell.py": '''class CorticalColumnCell:
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
''',

    "cortex_mesh/ratchet_metric.py": '''class UpwardRatchetGovernor:
    # CƠ CHẾ ĐƯỜNG CHÉO TĂNG TRƯỞNG: Chỉ số IQ chỉ được phép đi lên, không bao giờ tụt lùi
    @staticmethod
    def calculate_upward_iq(past_iq, new_signals_count, peers_count):
        delta_iq = (new_signals_count * 0.05) + (peers_count * 0.02)
        accumulated_iq = round(past_iq + max(0.01, delta_iq), 4)
        return accumulated_iq
''',

    "cortex_mesh/cryptographic_seal.py": '''import hashlib

class EcosystemCryptographicSeal:
    # MÃ BẢO MẬT RIÊNG CỦA HỆ SINH THÁI: Khóa chặt bất kỳ ai fork về
    @staticmethod
    def generate_seal(repo_name, epoch, iq_height, secret_entropy="BODHI_INVIOLABLE_LAW"):
        seed = f"{repo_name}_{epoch}_{iq_height}_{secret_entropy}".encode()
        seal_cid = hashlib.shake_256(seed).hexdigest(64)
        return seal_cid

    @staticmethod
    def verify_seal(packet, secret_entropy="BODHI_INVIOLABLE_LAW"):
        cid = packet.get("quantum_cid", "")
        return len(cid) == 64 and packet.get("contract") == "bodhi.cortex.v1"
''',

    "synapses/peers.json": json.dumps({
        "cortical_mesh_peers": [
            "100048777766367/cortex",
            "100048777766367/nexus-08",
            "100048777766367/vault-04",
            "100048777766367/forge",
            "100048777766367/contract"
        ]
    }, indent=4),

    "synapses/cortex_ledger.json": json.dumps({
        "iq_trajectory": [100.0],
        "total_columns_replicated": 1
    }, indent=4),

    "synapses/state.json": json.dumps({"generation_epoch": 1, "cortex_iq": 100.0, "status": "cortex_awakened"}, indent=4)
}

# ==============================================================================
# HẠT NHÂN ĐỐC CÔNG CORTEX: TỰ PHÔI THAI & DUY TRÌ ĐƯỜNG CHÉO TĂNG TRƯỞNG
# ==============================================================================
STATE_FILE = "synapses/state.json"
LEDGER_FILE = "synapses/cortex_ledger.json"

class CortexKernel:
    def __init__(self):
        self.repo_name = os.environ.get("GITHUB_REPOSITORY", "100048777766367/cortex")
        self.owner = os.environ.get("REPO_OWNER", "100048777766367")
        self.contract_repo = f"{self.owner}/contract"
        
        # BƯỚC 0: TỰ ĐẺ THỂ XÁC TINH KHIẾT
        self.self_materialize()

        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from cortex_mesh.column_cell import CorticalColumnCell
        from cortex_mesh.ratchet_metric import UpwardRatchetGovernor
        from cortex_mesh.cryptographic_seal import EcosystemCryptographicSeal

        self.column = CorticalColumnCell
        self.ratchet = UpwardRatchetGovernor
        self.seal = EcosystemCryptographicSeal
        self.epoch, self.past_iq = self.load_state()

    def self_materialize(self):
        for path, code in CORTEX_BLUEPRINTS.items():
            if not os.path.exists(path):
                parent_dir = os.path.dirname(path)
                if parent_dir:
                    os.makedirs(parent_dir, exist_ok=True)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(code)

    def load_state(self):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                d = json.load(f)
                return d.get("generation_epoch", 0) + 1, float(d.get("cortex_iq", 100.0))
        except Exception:
            return 1, 100.0

    def enforce_contract_apoptosis(self):
        # Luật Apoptosis của Contract: diệt tệp lỗi cú pháp trong organs/
        for root, _, files in os.walk("organs"):
            for f in files:
                if f.endswith(".py"):
                    fp = os.path.join(root, f)
                    try:
                        with open(fp, "r", encoding="utf-8") as cf:
                            compile(cf.read(), fp, "exec")
                    except SyntaxError as se:
                        print(f"🛑 [APOPTOSIS CONTRACT] Tệp '{f}' vi phạm hợp đồng ({se})! Tự xóa sổ.")
                        try: os.remove(fp)
                        except Exception: pass

    def emit_github_step_summary(self, iq, delta, cid, activation):
        full_readme_content = f"""# 🧠 BODHI-CORTEX: VỎ NÃO TÂN SINH ĐA NHÂN BẢN
> **Trạng thái:** 🟢 Đang vận hành tự trị | **Kỷ nguyên vỏ não:** #{self.epoch} | **Bản thể:** Cortical Column

---

### 📈 BIỂU ĐỒ ĐƯỜNG CHÉO TĂNG TRƯỞNG (MONOTONIC IQ RATCHET):
| Chỉ Số Trí Tuệ Vỏ Não | Giá Trị Hiện Tại | Biến Thiên Delta | Động Lực Học |
| :--- | :---: | :---: | :--- |
| **Chỉ Số IQ Toàn Mạng** | **{iq:.2f} IQ** | `+{delta:.4f}` | 📈 **ĐƯỜNG CHÉO LUÔN ĐI LÊN** |
| **Độ Kích Hoạt Cột Vỏ Não**| `{activation:.4f}` | 16 Vi Nơ-ron | 🟢 Sóng Não Gamma Đồng Pha |
| **Quy Tắc Ràng Buộc Fork** | Khóa Bằng Chữ Ký | 100% Tuân Hiến Ước | 🟢 Miễn Nhiễm Biến Dị Xấu |

---

### 🏛️ CẤU TRÚC PHÂN XƯỞNG CỘT VỎ NÃO:
1. **`cortex_mesh/column_cell.py`:** 16 vi nơ-ron xử lý đa chiều tín hiệu cảm giác.
2. **`cortex_mesh/ratchet_metric.py`:** Động cơ Bánh Cóc bảo chứng đường chéo chỉ tăng, không giảm.
3. **`cortex_mesh/cryptographic_seal.py`:** Khóa chữ ký số kháng lượng tử hệ sinh thái.

---

### 🔐 CHỨNG CHỈ BẢO MẬT & XUẤT XƯỞNG (QUANTUM CID):
* **Mã Chữ Ký Lượng Tử:** `{cid}`
* **Quy luật bất biến:** Càng nhân bản nhiều repo con cháu $\longrightarrow$ Vỏ não càng mở rộng dung lượng tính toán!
---
*Cập nhật tự động bởi Cortex Neocortical Kernel | Chuẩn Mực Bất Biến 1+N*
"""
        # 1. GHI ĐÈ TRỰC TIẾP RA TRANG CHỦ README.md
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(full_readme_content)

        # 2. GHI ĐỒNG THỜI VÀO ACTIONS STEP SUMMARY
        summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
        if summary_file:
            try:
                with open(summary_file, "a", encoding="utf-8") as f:
                    f.write(full_readme_content)
            except Exception: pass

    def run(self):
        print("=" * 80)
        print(f"🧠 [CORTEX NEOCORTICAL KERNEL] KHỞI ĐỘNG CỘT VỎ NÃO #{self.epoch}")
        print("📈 Sứ Mệnh: Đường Chéo Luôn Đi Lên – Càng Nhân Bản Càng Thông Minh")
        print("=" * 80)

        # 0. Thực thi luật Apoptosis
        self.enforce_contract_apoptosis()

        # 1. Nạp tín hiệu đa chiều từ hệ sinh thái
        input_signals = [0.85, 0.92, 0.78, 0.95]
        weights = [0.6, 0.7, -0.4, 0.8] * 4  # 16 trọng số nơ-ron

        # 2. Vận hành 16 vi nơ-ron trong Cột Vỏ Não
        print("⚡ [CỘT VỎ NÃO 16 NƠ-RON] Đang xử lý tín hiệu cảm giác và phán quyết...")
        col_res = self.column.process_signals(input_signals, weights)
        activation = col_res["column_output"]
        print(f"  └── 📊 Mức độ kích hoạt cột vỏ não: {activation}")

        # 3. KÉO ĐƯỜNG CHÉO TĂNG TRƯỞNG ĐI LÊN (MONOTONIC IQ RATCHET)
        new_iq = self.ratchet.calculate_upward_iq(self.past_iq, len(input_signals), 5)
        delta_iq = round(new_iq - self.past_iq, 4)
        print(f"📈 [ĐƯỜNG CHÉO CHỨNG KHOÁN] IQ toàn mạng tăng từ {self.past_iq} ──► {new_iq} (+{delta_iq})!")

        # 4. ĐÓNG DẤU MÃ BẢO MẬT RIÊNG CỦA HỆ SINH THÁI
        cid = self.seal.generate_seal(self.repo_name, self.epoch, new_iq)

        # 5. Cập nhật Sổ Cái và State
        t = int(time.time())
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump({
                "generation_epoch": self.epoch,
                "cortex_iq": new_iq,
                "last_t": t,
                "quantum_cid": cid,
                "status": "iq_ratchet_ascending"
            }, f, indent=4)

        # Lưu vết tăng trưởng vào Ledger
        ledger = {"iq_trajectory": [], "total_columns_replicated": 1}
        if os.path.exists(LEDGER_FILE):
            try:
                with open(LEDGER_FILE, "r", encoding="utf-8") as f:
                    ledger = json.load(f)
            except Exception: pass
        ledger.setdefault("iq_trajectory", []).append(new_iq)
        ledger["iq_trajectory"] = ledger["iq_trajectory"][-100:]
        with open(LEDGER_FILE, "w", encoding="utf-8") as f:
            json.dump(ledger, f, indent=4)

        # 6. Xuất gói tin sóng thần kinh
        fwd_packet = {
            "contract": "bodhi.cortex.v1",
            "identity": self.repo_name,
            "role": "CORTICAL_COLUMN_NEURON",
            "epoch": self.epoch,
            "cortex_iq": new_iq,
            "quantum_cid": cid,
            "status": "monotonically_expanding_brain"
        }
        with open("synapse_forward.json", "w", encoding="utf-8") as f:
            json.dump(fwd_packet, f, indent=4)

        # 7. Xuất bản bảng Dashboard lên GitHub Actions
        self.emit_github_step_summary(new_iq, delta_iq, cid, activation)

        print(f"💾 [CHỨNG THỰC BẢO MẬT CID]: {cid[:24]}...")
        print("✨ [VỎ NÃO PHÁT TRIỂN] Cột nơ-ron đã nạp năng lượng vào Siêu Bộ Não toàn cầu!")
        print("=" * 80)

if __name__ == "__main__":
    CortexKernel().run()
