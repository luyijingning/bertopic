# src/bp/config.py
from pathlib import Path

# bp/ 项目根
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# 数据目录：bp 同级目录下的 readme/
DATA_DIR = PROJECT_ROOT.parent / "readme"

# 输出目录
OUTPUT_DIR = PROJECT_ROOT / "output"
FIG_DIR = OUTPUT_DIR / "figures"
TABLE_DIR = OUTPUT_DIR / "tables"
MODEL_DIR = OUTPUT_DIR / "models"

for d in [OUTPUT_DIR, FIG_DIR, TABLE_DIR, MODEL_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# readme_1.csv ~ readme_20.csv
README_FILES = [DATA_DIR / f"readme_{i}.csv" for i in range(1, 21)]

# 组织信息文件（如果你有的话，没有就设 None）
ORG_FILE = None  # 例如 DATA_DIR / "org_info_detailed_202501161531.csv"

# 文本长度限制
README_MAX_CHARS = 8000

# 用于趋势分析的时间字段
TIME_COL_FOR_TREND = "created_at"   # 或 "updated_at"

# 主题模型
N_TOPICS_LDA = 20
BERT_EMBED_MODEL = "all-MiniLM-L6-v2"
SEMANTIC_THRESHOLD = 0.35