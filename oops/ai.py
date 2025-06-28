 
# # from transformers import pipeline
# # import logging

# # logging.basicConfig(level=logging.INFO)
# # logger = logging.getLogger(__name__)

# # def initialize_model():
# #     try:
# #         logger.info("Loading model...")
# #         pipe = pipeline(
# #             "text-generation",
# #             model="gpt2",  # Using GPT-2 instead of DistilGPT2
# #             max_length=100
# #         )
# #         return pipe
# #     except Exception as e
# #         logger.error(f"Model initialization failed: {str(e)}")
# #         return None

# # def generate_response(prompt, pipe):
# #     if not isinstance(prompt, str) or not prompt.strip():
# #         return "Error: Invalid prompt"
    
# #     try:
# #         logger.info("Generating response...")
# #         response = pipe(prompt,
# #                     max_length=150,
# #                     num_return_sequences=1,
# #                     temperature=0.7,  # Added temperature control
# #                     top_k=50,         # Added top_k sampling
# #                     top_p=0.95,       # Added nucleus sampling
# #                     truncation=True)
        
# #         # Clean up the response
# #         generated_text = response[0]['generated_text']
# #         # Remove the original prompt from the response
# #         if generated_text.startswith(prompt):
# #             generated_text = generated_text[len(prompt):].strip()
            
# #         return generated_text
# #     except Exception as e:
# #         logger.error(f"Response generation failed: {str(e)}")
# #         return f"Error: {str(e)}"

# # def main():
# #     pipe = initialize_model()
# #     if pipe is None:
# #         print("Failed to initialize model. Exiting...")
# #         return

# #     print("Enhanced Text Generation Model Ready (type 'quit' to exit)")
# #     print("Note: This is using GPT-2 with improved parameters for better responses")
    
# #     while True:
# #         try:
# #             prompt = input("\nEnter your prompt: ").strip()
            
# #             if prompt.lower() == 'quit':
# #                 print("Exiting...")
# #                 break
            
# #             if prompt:
# #                 print("\nGenerating response...")
# #                 response = generate_response(prompt, pipe)
# #                 print(f"\nResponse: {response}")
# #             else:
# #                 print("Please enter a valid prompt")
                
# #         except KeyboardInterrupt:
# #             print("\nExiting...")
# #             break
# #         except Exception as e:
# #             print(f"Error: {str(e)}")

# # if __name__ == "__main__":
# #     main()

# # from transformers import AutoTokenizer, AutoModelForCausalLM
# # import torch

# # def initialize_model():
# #     # Enable model parallelism
# #     device = "cuda" if torch.cuda.is_available() else "cpu"
    
# #     tokenizer = AutoTokenizer.from_pretrained(
# #         "nvidia/Llama-3.1-Nemotron-70B-Instruct-HF",
# #         device_map="auto",
# #         torch_dtype=torch.float16
# #     )
    
# #     model = AutoModelForCausalLM.from_pretrained(
# #         "nvidia/Llama-3.1-Nemotron-70B-Instruct-HF",
# #         device_map="auto",
# #         torch_dtype=torch.float16
# #     )
    
# #     return tokenizer, model

# # def generate_response(prompt, tokenizer, model):
# #     inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    
# #     outputs = model.generate(
# #         **inputs,
# #         max_length=200,
# #         temperature=0.7,
# #         do_sample=True
# #     )
    
# #     response = tokenizer.decode(outputs[0], skip_special_tokens=True)
# #     return response

# # def main():
# #     print("Initializing model...")
# #     tokenizer, model = initialize_model()
# #     print("Model ready!")
    
# #     while True:
# #         prompt = input("\nEnter prompt (or 'quit' to exit): ")
# #         if prompt.lower() == 'quit':
# #             break
            
# #         response = generate_response(prompt, tokenizer, model)
# #         print(f"\nResponse: {response}")

# # if __name__ == "__main__":
# #     main()

# from transformers import AutoTokenizer, AutoModelForCausalLM
# import torch

# def initialize_model():
#     # Enable model parallelism
#     device = "cuda" if torch.cuda.is_available() else "cpu"
    
#     tokenizer = AutoTokenizer.from_pretrained(
#         "nvidia/Llama-3.1-Nemotron-70B-Instruct-HF",
#         device_map="auto",
#         torch_dtype=torch.float16
#     )
    
#     model = AutoModelForCausalLM.from_pretrained(
#         "nvidia/Llama-3.1-Nemotron-70B-Instruct-HF",
#         device_map="auto",
#         torch_dtype=torch.float16
#     )
    
#     return tokenizer, model

# def generate_response(prompt, tokenizer, model):
#     inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    
#     outputs = model.generate(
#         **inputs,
#         max_length=200,
#         temperature=0.7,
#         do_sample=True
#     )
    
#     response = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     return response

# def main():
#     print("Initializing model...")
#     tokenizer, model = initialize_model()
#     print("Model ready!")
    
#     while True:
#         prompt = input("\nEnter prompt (or 'quit' to exit): ")
#         if prompt.lower() == 'quit':
#             break
            
#         response = generate_response(prompt, tokenizer, model)
#         print(f"\nResponse: {response}")

# if __name__ == "__main__":
#     main()


import cv2
from transformers import pipeline
from PIL import Image
import time
from collections import deque

# Initialize detector
detector = pipeline('object-detection',
                   model='hustvl/yolos-tiny',
                   device=-1
                   )

def get_iou(box1, box2):
    # Calculate intersection over union of two boxes
    x1 = max(box1['xmin'], box2['xmin'])
    y1 = max(box1['ymin'], box2['ymin'])
    x2 = min(box1['xmax'], box2['xmax'])
    y2 = min(box1['ymax'], box2['ymax'])
    
    intersection = max(0, x2 - x1) * max(0, y2 - y1)
    area1 = (box1['xmax'] - box1['xmin']) * (box1['ymax'] - box1['ymin'])
    area2 = (box2['xmax'] - box2['xmin']) * (box2['ymax'] - box2['ymin'])
    
    return intersection / (area1 + area2 - intersection)

def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    print("Starting webcam detection... Press 'q' to quit")
    
    # Frame rate control
    fps_target = 10  # Reduced target FPS
    frame_interval = 1.0 / fps_target
    last_frame_time = time.time()
    
    # Detection smoothing
    previous_detections = []
    detection_history = deque(maxlen=3)  # Keep last 3 frames of detections
    
    while True:
        current_time = time.time()
        if current_time - last_frame_time < frame_interval:
            continue
            
        ret, frame = cap.read()
        if not ret:
            break
            
        frame = cv2.resize(frame, (640, 480))
        
        try:
            pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            current_detections = detector(pil_image)
            
            # Add current detections to history
            detection_history.append(current_detections)
            
            # Smooth detections across frames
            stable_detections = []
            if current_detections:
                for det in current_detections:
                    # Check if similar detection exists in previous frames
                    found_in_previous = False
                    for prev_frame in list(detection_history)[:-1]:
                        for prev_det in prev_frame:
                            if (det['label'] == prev_det['label'] and 
                                get_iou(det['box'], prev_det['box']) > 0.3):
                                found_in_previous = True
                                break
                        if found_in_previous:
                            break
                    
                    if found_in_previous or det['score'] > 0.4:  # Higher confidence threshold
                        stable_detections.append(det)
            
            # Draw stable detections
            for detection in stable_detections:
                box = detection['box']
                label = f"{detection['label']}: {round(detection['score']*100, 1)}%"
                
                x, y = int(box['xmin']), int(box['ymin'])
                x2, y2 = int(box['xmax']), int(box['ymax'])
                
                # Draw thicker box and add background to text
                cv2.rectangle(frame, (x, y), (x2, y2), (0, 255, 0), 3)
                
                # Add background rectangle for text
                (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
                cv2.rectangle(frame, (x, y-25), (x+w, y), (0, 255, 0), -1)
                cv2.putText(frame, label, (x, y-5), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        
        except Exception as e:
            print(f"Error in detection: {e}")
            
        cv2.imshow('Object Detection', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
        last_frame_time = current_time
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()