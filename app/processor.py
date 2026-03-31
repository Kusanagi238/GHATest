def calculate_average_temp(temperatures: list[float] | None) -> float:
    """计算平均温度"""
    if not temperatures:
        return 0.0
    return sum(temperatures) / len(temperatures)

def parse_weather_config(config: dict) -> str:
    """解析配置并返回状态"""
    # 故意留一个没用的 import 触发 Lint 错误 (实验用)
    import os 
    
    if "region" not in config:
        raise ValueError("Missing 'region' in config")
    return f"Processing region: {config['region']}"