.. _Docker:

Fluidigm2PURC on Docker
=======================

We have made the Fluidigm2PURC pipeline available as a Docker image in the hopes that it will
facilitate its use by providing all dependencies pre-installed. This also allows any researcher
with the Docker software installed on their computer to use our pipeline
(e.g., Fluidigm2PURC won't work on Windows without using Docker). Details on Docker itself
can be found on the main website: `link <https://www.docker.com/>`_.

To obtain the Fluidigm2PURC image, first download Docker for your computer
(if you haven't already done so). Then, launch a terminal window and use the following
commands to get the software:

.. code:: bash

  docker pull pblischak/fluidigm2purc

To run an analysis with Fluidigm2PURC, launch a Docker container that is running the
Fluidigm2PURC image:

.. code:: bash

  docker run -it pblischak/fluidigm2purc

The above line of code will get you running inside a Docker container with everything
that you need to run Fluidigm2PURC. However, you will also need to link your local files
to the container. This can be done using the ``-v`` option. To start, navigate to the folder
with your paired-end reads (R1 and R2) that you want to analyze with Fluidigm2PURC. Then,
use this command to link that folder to the Docker container running Fluidigm2PURC:

.. code:: bash

  docker run -it -v $(pwd):/home pblischak/fluidigm2purc

If you type ``ls``, you should see your files available for analyzing. All analyses that you
run in the container will also write those files to the directory from which you launched the container.
This way, everything that you do will automatically be available on your computer outside
of Docker.
