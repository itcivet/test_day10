import yaml


def build_login_data():


    with open("../data/login_data.yaml", encoding="utf-8")as f:
        data = yaml.safe_load(f)
        data_list = list()
        for i in data:
            data_list.append((i.get("num"),
                              i.get("pwd")))
        print(data_list)
        return data_list # 返回参数数据
