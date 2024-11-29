clear
close all

%一軸引張り試験片の有限要素法解析
%機械工学実験テキスト
%Programed by Y.N ;Mar.9,1995
%Translated to Matlab by H.K ;Mar.8,2020

%定数の定義
ne = 3; %有限要素数
nn = 4; %自由度: 全体剛性マトリックスの大きさ

%%グローバル変数の定義
fe = [0,1,1,1]; %外力既知接点節点番号(未知と既知による場合分け)
fk = [0.0,0.0,0.0,100.0] ; %外力既知接点変位または外力ベクトル
%g(ne) ; %要素の剛性率
kd = zeros(nn); %全体剛性マトリックス
%kt(nn,nn+1) ; %全体剛性方程式組換え後の係数行列
uk = [0.0,0.0,0.0,0.0] ; %全体剛性方程式組換え後の右辺
%u(nn) ; %変位ベクトル
%f(nn) ; %節点力ベクトル
A = [200.0,100.0,200.0]; %各要素の断面積
L = [50.0,100.0,50.0]; %各要素の長さ
E = [2.0e5,2.0e5,2.0e5]; %各要素のヤング率

%%データの入力
for i = 1:ne
    g(i) = A(i)*E(i)/L(i); %剛性率計算
end

%%要素剛性マトリックスの計算
for i = 1:2
    for j = 1:2
        ke(i,j) = (-1.0)^(i+j);        
    end
end

%%全体剛性マトリックスの合成
for n = 2:ne+1
    for i = 1:2
        for j = 1:2
            n1 = n-2;
            ki = n1+i;
            kj = n1+j;
            kd(ki,kj) = kd(ki,kj) + g(n-1)*ke(i,j);
        end
    end
end

%%全体剛性方程式組の組換え（境界条件の考慮）
for i = 1:nn
    for j = 1:nn
        if fe(j) == 0 %未知（グローバル変数）
            if i==j
                kt(i,j) = -1.0;
            else
                kt(i,j) = 0.0;
            end
        else %既知（グローバル変数）
            kt(i,j) = kd(i,j);
        end
    end
    for k=1:nn
        if fe(k) == 0
            f(i) = -kd(i,k)*uk(k);
        else
            f(i) = fk(i)-kd(i,k)*uk(k);
        end
    end
end

%%未知力および未知変位の導出（ガウスの消去法）（掃き出し法）
for ii = 1:nn
    kt(ii,nn+1) = f(ii);
end

for kk = 1:nn
    flag = 0;
    for ii = kk:nn
        if kt(ii,kk) ~= 0.0 %ノットイコール

        p = kt(ii,kk);
    for jj = kk:nn+1
        a1 = kt(kk,jj);
        kt(kk,jj) = kt(ii,jj);
        kt(ii,jj) = a1/p;
    end
    for ii = 1:nn
        if ii ~= kk
            qq = kt(ii,kk);
            for jj = kk:nn+1
                kt(ii,jj) = kt(ii,jj)-qq*kt(kk,jj);
            end
        end
    end

            flag = 1;
            ii = nn+1;
        end
    end
    if flag == 0
        kk = nn+1;
    end
end

%%ひずみおよび応力の計算
for m = 1:nn
    if fe(m) == 0
        u(m) = 0.0;
    else
        u(m) = kt(m,nn+1);
    end
end %変位の計算
for mn = 1:ne
    ee(mn) = (u(mn+1)-u(mn))/L(mn);
end %ひずみの計算
for mn = 1:ne
    ss(mn) = E(mn)*ee(mn);
end %応力の計算
       