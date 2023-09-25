from flask import Flask, render_template, request
import diffusion_inference

# make our Flask api...
app = Flask(__name__, template_folder="template")


# form urls/...
@app.route("/")
def home():
    # full_filename = os.path.join('static', 'images', 'tes.png')
    return render_template("rm.html")


# Accepting form data
@app.route("/prediction", methods=["POST"])
def prediction():
    import Dashauth
    q = request.form["username"]
    w = request.form["pass"]
    e = request.form["city"]
    some_name = q
    some_value = w
    prompt = "Create a high-definition realistic image of a beautifully presented {}, capturing all the " \
             "intricate details " \
             "and vibrant colors to make it look as appetizing as possible.".format(e)
    image = diffusion_inference.generate_image(prompt)
    diffusion_inference.save_generated_image(image, "static/image.jpg")

    if some_name in Dashauth.VALID_USERNAME_PASSWORD_PAIRS.keys() and \
            some_value in Dashauth.VALID_USERNAME_PASSWORD_PAIRS.values():
        return render_template("rm1.html")
        # return render_template("rm1.html", user_image="template/static/images/test.png")
    else:
        return "Credentials do not match!"


# Run this file as the main file...
if __name__ == "__main__":
    app.run(debug=True)

# A photorealistic image of New York City at night, with neon lights and skyscrapers.
# An abstract cityscape in the style of Wassily Kandinsky, with swirling lines and shapes in bold colors.
# A surrealistic cityscape with dreamlike elements, such as floating buildings and talking animals.
# A vibrant, colorful cityscape with the energy and dynamism of Nighthawks by Edward Hopper.
# A dark, moody cityscape with the foreboding atmosphere of Blade Runner.

# import os
# from flask import Flask, render_template
#
# app = Flask(__name__, template_folder="template", static_url_path='/static/images')
#
#
# @app.route('/')
# # @app.route('/index')
# def show_index():
#     # user_image="static/images/tes.png"
#     full_filename = os.path.join('static', 'images', 'tes.png')
#     return render_template("index.html", user_image=full_filename)
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
