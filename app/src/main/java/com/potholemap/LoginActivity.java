package com.potholemap;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class LoginActivity extends AppCompatActivity {

    private static final String ADMIN_USER = "admin";
    private static final String ADMIN_PASS = "1234";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        EditText username = findViewById(R.id.username);
        EditText password = findViewById(R.id.password);

        Button adminBtn = findViewById(R.id.btnAdminLogin);
        Button guestBtn = findViewById(R.id.btnGuest);

        // 🔐 ADMIN LOGIN
        adminBtn.setOnClickListener(v -> {
            String u = username.getText().toString().trim();
            String p = password.getText().toString().trim();

            if (u.equals(ADMIN_USER) && p.equals(ADMIN_PASS)) {

                SharedPreferences prefs = getSharedPreferences("admin", MODE_PRIVATE);
                prefs.edit().putBoolean("logged", true).apply();

                Intent i = new Intent(this, MainActivity.class);
                i.putExtra("ROLE", "ADMIN");
                startActivity(i);
                finish();

            } else {
                Toast.makeText(this, "Invalid admin credentials", Toast.LENGTH_SHORT).show();
            }
        });

        // 👤 GUEST / USER LOGIN (NO PASSWORD)
        guestBtn.setOnClickListener(v -> {
            Intent i = new Intent(this, MainActivity.class);
            i.putExtra("ROLE", "USER");
            startActivity(i);
            finish();
        });
    }
}
