from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    videos = []
    for root, dirs, files in os.walk('static/bigdisk/movies'):
        for file in files:
            if file.endswith(('.mkv','.mp4')):
                video_path = os.path.join(root, file)
                video_name = os.path.splitext(file)[0]
                subtitle_path = None
                for s_file in files:
                    if s_file.endswith('.srt') and s_file.startswith(video_name):
                        subtitle_path = os.path.join(root, s_file)
                videos.append({'video_path': video_path, 'subtitle_path': subtitle_path, 'video_name': video_name})
    return render_template('index.html', videos=videos)

if __name__ == '__main__':
    app.run(port='80', debug=True)
