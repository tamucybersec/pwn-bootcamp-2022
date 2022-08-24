FROM debian:buster-slim as build

ARG name

RUN apt-get update -y; apt-get install build-essential libseccomp-dev -y
ADD $name.c /tmp/$name.c
ADD Makefile /tmp/Makefile
RUN cd /tmp/; make all

FROM debian:buster-slim

ARG name
ARG port

RUN apt-get update -y; apt-get install socat seccomp patchelf -y
COPY --from=build /tmp/$name /pwn/$name
COPY flag.txt /pwn/flag.txt
WORKDIR /pwn

EXPOSE $port

RUN echo "exec socat -s TCP-LISTEN:$port,reuseaddr,fork EXEC:/pwn/$name,stderr" > /pwn/docker_entrypoint.sh
RUN cp /lib/x86_64-linux-gnu/ld-2.28.so /pwn/ld-linux-x86-64.so.2 && cp /lib/x86_64-linux-gnu/libc-2.28.so /pwn/libc.so.6
RUN patchelf --set-rpath . /pwn/echo3 && patchelf --set-interpreter ld-linux-x86-64.so.2 /pwn/echo3
ENTRYPOINT ["sh", "/pwn/docker_entrypoint.sh"]