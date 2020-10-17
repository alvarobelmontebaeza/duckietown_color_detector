FROM duckietown/dt-duckiebot-interface:daffy-arm32v7

WORKDIR /duckietown_color_detector

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

RUN export N_SPLITS = 2

COPY color_detector.py .

CMD python3 ./color_detector.py