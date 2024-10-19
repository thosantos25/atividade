package senai;

import javax.swin.JOptionPane;
public class ExemploRecursivo2 {
public static int somarPares(int numero){
        if(numero == 0){
        return 0;
    }
    if(numero % 2 == 0){
        return numero + somarPares(numero - 1);
    } else {
        return somarPares(numero - 1):
    }
    public static void main(String[] args) {
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite um número"));
        System.out.println(somarPares(numero));
        }
    }   