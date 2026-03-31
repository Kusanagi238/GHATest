import json
import sys
from app.processor import calculate_average_temp, parse_weather_config

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m app.main '{\"region\": \"Taichung\", \"temps\": [20.5, 22.0, 24.5]}'")
        sys.exit(1)
        
    try:
        # 解析传入的 JSON 字符串参数
        input_data = json.loads(sys.argv[1])
        
        # 处理配置和计算逻辑
        status = parse_weather_config(input_data)
        avg_temp = calculate_average_temp(input_data.get("temps"))
        
        # 输出结果
        print(status)
        print(f"Average temperature: {avg_temp:.2f}°C")
        
    except json.JSONDecodeError:
        print("Error: Invalid JSON input.")
        sys.exit(1)
    except ValueError as e:
        print(f"Configuration Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()