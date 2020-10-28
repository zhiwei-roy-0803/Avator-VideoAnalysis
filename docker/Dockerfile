FROM czw666/avator:base

# Copy source
RUN rm -rf content
COPY . content

# Set Environment Variables
ENV CONDA_ROOT=/miniconda
ENV PATH=${CONDA_ROOT}/bin:/usr/local/cuda:${PATH}
ENV CONDA_AUTO_UPDATE_CONDA=false
ENV PYTHONPATH=$PYTHONPATH:/content/hysia

WORKDIR content

#ENTRYPOINT ["/bin/bash", "/content/scripts/docker_entry.sh"]
