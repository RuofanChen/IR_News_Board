import csv
from string import Template

# read template
def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def read_news_j(newsFile):
    import json
    f = open(newsFile)
    data = json.load(f)
    # since id is unique for each news, so let id be the key
    dataset = {}
    for i in range(len(data['data'])):
        new_key = data['data'][i]['id']
        dataset[new_key]=data['data'][i]
    return dataset



def main():
    news_template = read_template('../news_template.txt')
    news_data = read_news_j('../2022-2-news.json')
    for key in news_data:
        news_generate = news_template.substitute(title=news_data[key]['title'],abstract=news_data[key]['abstract'],nyt_url=news_data[key]['url'],text=news_data[key]['text'])
        file_name = key + '.html'
        f = open(file_name,'w',encoding="utf-8")
        f.write(news_generate)
        f.close()

if __name__ == '__main__':
    main()

