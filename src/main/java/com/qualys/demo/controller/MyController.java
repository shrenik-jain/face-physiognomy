package com.qualys.demo.controller;


import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController

public class MyController {
	
	@GetMapping("/getdisplay")
	public String display() {
		
		return "hello";
		
	}
	

 }
