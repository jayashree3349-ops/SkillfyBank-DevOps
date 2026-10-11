FROM eclipse-temurin:21-jdk-alpine AS build
WORKDIR /src
COPY src ./src
RUN javac --add-modules jdk.httpserver \
    -d out src/main/java/com/skillfybank/transaction/TransactionApplication.java

FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY --from=build /src/out ./out
EXPOSE 8081
CMD ["java", "--add-modules", "jdk.httpserver", "-cp", "out", "com.skillfybank.transaction.TransactionApplication"]
