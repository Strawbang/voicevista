package com.example.serverservice.infrastructure.controllers;

import com.example.serverservice.application.services.ServerService;
import com.example.serverservice.domain.entities.Server;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/servers")
public class ServerController {
    private final ServerService serverService;

    public ServerController(ServerService serverService) {
        this.serverService = serverService;
    }

    @GetMapping
    public List<Server> getAllServers() {
        return serverService.findAll();
    }

    @PostMapping
    public ResponseEntity<Server> createServer(@RequestBody Server server) {
        Server savedServer = serverService.save(server);
        return ResponseEntity.status(201).body(savedServer);
    }
}