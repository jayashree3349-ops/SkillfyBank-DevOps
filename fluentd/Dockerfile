FROM fluent/fluentd:v1.16-debian-1
USER root
RUN gem install elasticsearch -v 6.0.2 --no-document \
 && gem install fluent-plugin-elasticsearch -v 6.0.0 --no-document \
 && gem install fluent-plugin-parser-cri --no-document \
 && gem uninstall elasticsearch -v 9.5.0 -x -I
USER fluent
