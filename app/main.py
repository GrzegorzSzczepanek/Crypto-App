from modules.test import StopwatchApp
import modules.data_collection as dc

if __name__ == "__main__":
    print("Starting...")
    # print(list(dc.get_all_token_info_by_id("bitcoin").items())[:10])
    print(dc.get_supported_vs_currencies())
    # print(dc.get_simple_price())
