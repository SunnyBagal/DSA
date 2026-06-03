from PIL import Image
import face_recognition

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("/Users/sunny/Python/CS50/Office.jpg")

# Find all the faces in the image using the default HOG-based model
face_locations = face_recognition.face_locations(image)

print(f"Found {len(face_locations)} face(s) in this photograph.")

for face_location in face_locations:
    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print(f"A face is located at pixel location Top: {top}, Left: {left}, Bottom: {bottom}, Right: {right}")

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    
    # Create a PIL image object from the numpy array
    pil_image = Image.fromarray(face_image)
    
    # Show the temporary image
    pil_image.show() 