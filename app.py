from flask import Flask, request, jsonify, send_file
from pathlib import Path
import torch
import subprocess
import os
import uuid

app = Flask(__name__)

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

DEVICE = "cpu"

@app.route("/")
def index():
    return "Stable Video Diffusion CPU server is running!"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    video_filename = OUTPUT_DIR / f"{uuid.uuid4().hex}.mp4"

    try:
        subprocess.run([
            "python", "-m", "stable_video_diffusion",
            "--prompt", prompt,
            "--output", str(video_filename),
            "--device", DEVICE,
            "--num-frames", "16",
            "--fps", "4"
        ], check=True)
    except subprocess.CalledProcessError as e:
        return jsonify({"error": "Video generation failed", "details": str(e)}), 500

    return send_file(video_filename, mimetype="video/mp4")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
