from dotenv import load_dotenv
import os
import requests
import json
import inquirer
load_dotenv()
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
models = {
        'deepseek-v3-0324:free':'deepseek/deepseek-chat-v3-0324:free',
        'gemini-2.0-flash-exp:free':'google/gemini-2.0-flash-exp:free',
        'qwen3-235b-a22b:free':'qwen/qwen3-235b-a22b:free',
        'microsoft-mai-ds-r1:free':'microsoft/mai-ds-r1:free',
        'mistral-devstral-small:free':'mistralai/devstral-small:free',
        'meta-llama-4-maverick:free':'meta-llama/llama-4-maverick:free',
        'nvidia-llama-3.1-nemotron-ultra-253b-v1:free':'nvidia/llama-3.1-nemotron-ultra-253b-v1:free',
        'moonshotai-moonlight-16b-a3b-instruct:free':'moonshotai/moonlight-16b-a3b-instruct:free',
        'qwerky-72b:free':'featherless/qwerky-72b:free'
    }
messages = []
def main():
    
    modelList = [keys for keys in models.keys()]
    questions = [
         inquirer.List(
            "model_name",
            choices=modelList,
            message="Select any model"
         ),
         
    ]    
    selected_model = inquirer.prompt(questions=questions)
    while True:
      query = input("Ask LLM (type 'quit' to exit): ").strip()
      if query.lower() == 'quit':
            print("Exiting...")
            break
      if not query:
            print("Please enter a valid query.")
            continue
      result = ask_llm(query=query,model_name=selected_model['model_name'])
      if 'choices' in result:   
        print(result['choices'][0]['message']['content'])
      else:
            print(f"Error: {result}")
      # query = input("Write any query by selecting model")

def ask_llm(query:str,model_name:str):
        try:
          
          messages.append(
              {
                  'role':"user","content":query
              }
          )
          get_model = models[model_name]
          response = requests.post(
              url="https://openrouter.ai/api/v1/chat/completions",
              headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
              },
              data=json.dumps({
                "model":get_model,
                "messages": messages
              }),
              
          )
          result =  response.json()
          if 'choices' in result:
            messages.append({
                "role": "model",
                "content": result['choices'][0]['message']['content']
            })
            # print(messages)
          return result
    
        except Exception as e:
          return(e)
if __name__ == "__main__":
    main()
