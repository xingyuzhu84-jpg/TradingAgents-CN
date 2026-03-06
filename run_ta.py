import os
os.environ['DASHSCOPE_API_KEY'] = 'sk-sp-ae6f1b9f26654904a759ff3554d799d0'
os.environ['MONGODB_ENABLED'] = 'false'
os.environ['REDIS_ENABLED'] = 'false'

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

config = DEFAULT_CONFIG.copy()
config['llm_provider'] = 'dashscope'
config['deep_think_llm'] = 'qwen-plus'
config['quick_think_llm'] = 'qwen-turbo'
config['max_debate_rounds'] = 1

ta = TradingAgentsGraph(debug=True, config=config)
result, decision = ta.propagate('600938', '2026-03-06')
print('=== 分析结果 ===')
print(decision)
