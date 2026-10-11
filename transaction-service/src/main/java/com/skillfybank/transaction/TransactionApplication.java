
package com.skillfybank.transaction;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@SpringBootApplication
public class TransactionApplication {

    public static void main(String[] args) {
        SpringApplication.run(TransactionApplication.class, args);
    }

    @RestController
    static class TransactionController {

        @GetMapping("/")
        public Map<String, String> home() {
            return Map.of(
                "service", "SkillfyBank Transaction Service",
                "status", "running"
            );
        }

        @GetMapping("/health")
        public Map<String, String> health() {
            return Map.of("status", "healthy");
        }
    }
}
