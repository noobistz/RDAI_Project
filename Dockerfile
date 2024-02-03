FROM pytorch/pytorch:2.2.0-cuda12.1-cudnn8-runtime

RUN apt-get update
RUN apt install wget -y
RUN mkdir -p /opt/miniconda3
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /opt/miniconda3/miniconda.sh
RUN bash /opt/miniconda3/miniconda.sh -b -u -p /opt/miniconda3
RUN rm -rf /opt/miniconda3/miniconda.sh
RUN /opt/miniconda3/bin/conda init

RUN mkdir -p ~/app 
WORKDIR /app
COPY * ./ 

# Create the environment
RUN /opt/miniconda3/bin/conda env create -f environment.yml 

ENV PATH /opt/miniconda3/bin:$PATH

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "rdai", "/bin/bash", "-c"]

# Expose 8000 for API
EXPOSE 8000

# Run the software 
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "rdai", "python", "-m" , "uvicorn", "main:app", "--host", "0.0.0.0", "--reload", "--port", "8000"]