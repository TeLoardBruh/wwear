import 'package:flutter/material.dart';
import 'package:wwear/components/auth.dart';

void main() {
  runApp(
    const MaterialApp(
      home: Scaffold(
        backgroundColor: Color(0xFFF3EFF5),
        body: AuthComponents(
            buttonActionTitle: "Sign Up",
            imageUrl: 'assets/image/signup.png',
            welcomeText: 'Hello Again!',
            subHeader1: 'Welcome back you’ve',
            subHeader2:
                'Welcome to WWear we would like to recommend best suited outift for you!'),
      ),
    ),
  );
}
