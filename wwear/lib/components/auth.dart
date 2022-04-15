import 'package:flutter/material.dart';

class AuthComponents extends StatelessWidget {
  final String? buttonActionTitle;
  final String? imageUrl;
  final String? welcomeText;
  final String? subHeader1;
  final String? subHeader2;

  const AuthComponents({
    Key? key,
    this.buttonActionTitle,
    this.imageUrl,
    this.subHeader1,
    this.subHeader2,
    this.welcomeText,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        SafeArea(
          child: Image(
            image: AssetImage(imageUrl!),
          ),
        ),
        Text(
          welcomeText!,
          style: const TextStyle(fontSize: 36, fontWeight: FontWeight.w500),
        ),
        const SizedBox(
          height: 10,
        ),
        Text(
          subHeader1!,
          style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w400),
        ),
        Text(
          subHeader2!,
          style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w400),
        ),
        Container(
          margin: const EdgeInsets.only(left: 25.0, right: 25.0, top: 10.0),
          child: Column(
            children: [
              TextField(
                decoration: InputDecoration(
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(10),
                  ),
                  hintText: 'User name',
                ),
              ),
              const SizedBox(height: 10),
              TextField(
                decoration: InputDecoration(
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(10),
                  ),
                  hintText: 'Password',
                ),
              ),
              const SizedBox(
                height: 25,
              ),
              SizedBox(
                  width: double.infinity,
                  child: ElevatedButton(
                    style: ElevatedButton.styleFrom(
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(15.0),
                      ),
                      padding: const EdgeInsets.symmetric(
                          horizontal: 50, vertical: 20),
                      primary: const Color(0xFFFC6B68),
                      textStyle: const TextStyle(
                          fontSize: 20, fontWeight: FontWeight.w700),
                    ),
                    onPressed: () {},
                    child: Text(buttonActionTitle!),
                  )),
            ],
          ),
        )
      ],
    );
  }
}
