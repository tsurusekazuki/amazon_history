from selenium import webdriver
import settings
import time
import pandas as pd


ID = settings.ID
PASS = settings.PASS
CHROME_PATH = settings.CHROME_PATH
print(CHROME_PATH)


def main():
    driver = webdriver.Chrome(executable_path=CHROME_PATH)
    driver.get("https://www.amazon.co.jp/gp/css/order-history?ref_=nav_orders_first")
    time.sleep(5)

    driver.find_element_by_id('ap_email').send_keys(ID)
    driver.find_element_by_id('continue').click()
    print("ユーザーID認証成功")
    driver.find_element_by_id("ap_password").send_keys(PASS)
    driver.find_element_by_id('signInSubmit').click()
    print("パスワード認証成功")
    print("注文履歴ページ")
    current_url = driver.current_url
    print(current_url)

    # 遷移先のページのurlを集め、リストに格納する
    links = driver.find_element_by_class_name("a-pagination")
    link = links.find_elements_by_tag_name("a")
    url_list = []
    for l in link:
        url = l.get_attribute("href")
        url_list.append(url)

    dic = {}

    # 各ページから商品の名前とその商品のurlを取得し辞書に格納する
    for url in url_list:
        print("-------------------------------------------------")
        print(url)
        driver.get(url)
        element = driver.find_elements_by_class_name("a-link-normal")
        for elem in element:
            if "注文の詳細" not in elem.text:
                pdt_url = elem.get_attribute("href")
                dic[elem.text] = pdt_url

    print("ロード完了")

    # 辞書をcsvに書き出し
    df = pd.DataFrame({"商品名": list(dic.keys()), "URL": list(dic.values())})
    df.to_csv("./data.csv", encoding='utf_8_sig')

    driver.close()


if __name__ == '__main__':
    main()
