from zhipuai import ZhipuAI
import time 
client = ZhipuAI(api_key="dc5e8a03e0c63df039d51bf815e145a5.4hV29Msqrd2exp3o") # 请填写您自己的APIKey
response = client.chat.asyncCompletions.create(
    model="glm-4",  # 填写需要调用的模型名称
    messages=[
        {
            "role": "user",
            "content": "请你作为童话故事大王，写一篇短篇童话故事，故事的主题是要永远保持一颗善良的心，要能够激发儿童的学习兴趣和想象力，同时也能够帮助儿童更好地理解和接受故事中所蕴含的道理和价值观。"
        }
    ],
)
time.sleep(2)
print(response)