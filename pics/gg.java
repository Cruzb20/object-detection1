import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

import java.awt.*;
import java.awt.Image;

public class gg {
    public static void main(String[] args) {
        // Lumikha ng isang bagong frame
        JFrame frame = new JFrame("Icon Example");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(null); // Tanggalin ang default na layout manager
        
          JLabel label1 = new JLabel("USERNAME: ");
        label1.setBounds(30, 60, 120, 30);
         label1.setFont(new Font("Mongolian Baiti", Font.BOLD, 18));

        // Lumikha ng isang label at maglagay ng icon
        ImageIcon icon = new ImageIcon("img1.png");
        Image image = icon.getImage().getScaledInstance(70, 70, Image.SCALE_SMOOTH);
        ImageIcon resizedIcon = new ImageIcon(image);
        JLabel label = new JLabel(resizedIcon);
        label.setBounds(150, 60, 50, 30);
        
        JTextField t1 = new JTextField();
        t1.setBounds(200, 60, 210, 30);
        t1.setBorder(null); // Tanggalin ang border
        t1.setBorder(BorderFactory.createMatteBorder(0, 0, 3, 0, Color.BLACK)); // Magdagdag ng border sa ibaba
        
        // Itakda ang sukat ng frame at ipakita ito
        frame.add(label); frame.add(label1);
        frame.add(t1);
        frame.setSize(500, 500);
        frame.setVisible(true);
    }
}






