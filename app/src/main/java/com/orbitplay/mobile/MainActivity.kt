package com.orbitplay.mobile

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

private val Background = Color(0xFF090D18)
private val Panel = Color(0xFF151D2D)
private val Accent = Color(0xFF38BDF8)

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { OrbitApp() }
    }
}

@Composable
private fun OrbitApp() {
    var arabic by remember { mutableStateOf(true) }
    var resolution by remember { mutableStateOf("720p") }
    var status by remember { mutableStateOf(if (arabic) "جاهز للاتصال بالشبكة المحلية" else "Ready for local network") }
    val title = if (arabic) "ORBIT PLAY" else "ORBIT PLAY"
    val subtitle = if (arabic) "بث PS5 عبر شبكة Wi-Fi المحلية" else "PS5 streaming over local Wi-Fi"
    MaterialTheme(colorScheme = darkColorScheme(
        background = Background, surface = Panel, primary = Accent,
        onBackground = Color.White, onSurface = Color.White
    )) {
        Column(
            modifier = Modifier.fillMaxSize().background(Background).padding(22.dp),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.End) {
                TextButton(onClick = { arabic = !arabic; status = if (arabic) "جاهز للاتصال بالشبكة المحلية" else "Ready for local network" }) {
                    Text(if (arabic) "English" else "العربية", color = Accent)
                }
            }
            Spacer(Modifier.height(38.dp))
            Text(title, fontSize = 31.sp, fontWeight = FontWeight.Black, color = Accent)
            Spacer(Modifier.height(8.dp))
            Text(subtitle, color = Color.LightGray, fontSize = 14.sp)
            Spacer(Modifier.height(34.dp))
            Card(colors = CardDefaults.cardColors(containerColor = Panel), shape = RoundedCornerShape(22.dp)) {
                Column(Modifier.fillMaxWidth().padding(20.dp)) {
                    Text(if (arabic) "إعدادات البث" else "STREAM SETTINGS", color = Accent, fontWeight = FontWeight.Bold)
                    Spacer(Modifier.height(16.dp))
                    Text(if (arabic) "الدقة" else "Resolution", color = Color.LightGray)
                    Spacer(Modifier.height(8.dp))
                    Row(horizontalArrangement = Arrangement.spacedBy(10.dp)) {
                        FilterChip(selected = resolution == "720p", onClick = { resolution = "720p" }, label = { Text("720p") })
                        FilterChip(selected = resolution == "1080p", onClick = { resolution = "1080p" }, label = { Text("1080p") })
                    }
                    Spacer(Modifier.height(12.dp))
                    Text(if (arabic) "معدل الإطارات: 30 FPS" else "Frame rate: 30 FPS", color = Color.LightGray)
                    Text(if (arabic) "الاتصال: Wi-Fi محلي فقط" else "Connection: local Wi-Fi only", color = Color.LightGray)
                }
            }
            Spacer(Modifier.height(22.dp))
            Button(
                onClick = { status = if (arabic) "محرك Remote Play لم يُدمج بعد" else "Remote Play engine is not integrated yet" },
                modifier = Modifier.fillMaxWidth().height(54.dp),
                colors = ButtonDefaults.buttonColors(containerColor = Accent),
                shape = RoundedCornerShape(16.dp)
            ) {
                Text(if (arabic) "اتصال بـ PS5" else "Connect to PS5", color = Color(0xFF06111D), fontWeight = FontWeight.Bold)
            }
            Spacer(Modifier.height(16.dp))
            Text(status, color = Color(0xFFFFC66D), fontSize = 13.sp)
            Spacer(Modifier.weight(1f))
            Text(if (arabic) "نسخة أولية 0.1.0 • لا يوجد بث فعلي حتى دمج محرك Chiaki-ng" else "Prototype 0.1.0 • Live streaming requires Chiaki-ng engine integration", color = Color.Gray, fontSize = 11.sp)
        }
    }
}
