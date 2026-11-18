import React from "react";
import {
  AbsoluteFill,
  Audio,
  Img,
  Sequence,
  interpolate,
  staticFile,
  useCurrentFrame,
} from "remotion";

type ShortVideoProps = {
  logoAsset: string | null;
  voiceoverAsset: string | null;
};

type SceneProps = {
  overlay: string;
  dialogue: string;
  children?: React.ReactNode;
};

const COLORS = {
  ink: "#18304a",
  blue: "#4b7bec",
  paleBlue: "#e7f0ff",
  yellow: "#ffd166",
  cream: "#fffaf0",
  green: "#5da987",
  muted: "#6d7f91",
  white: "#ffffff",
};

const scenes = [
  {
    from: 0,
    duration: 150,
    overlay: "Angka banyak. Mulai dari mana?",
    dialogue:
      "Punya banyak angka, tapi bingung mau cerita apa? Aku mulai dari satu pertanyaan.",
    kind: "hook",
  },
  {
    from: 150,
    duration: 210,
    overlay: "Pertanyaan dulu",
    dialogue:
      "Ini lima transaksi kantin fiktif. Pertanyaanku: menu apa yang paling sering tercatat?",
    kind: "transactions",
  },
  {
    from: 360,
    duration: 270,
    overlay: "3 dari 5 transaksi",
    dialogue:
      "Nasi Ayam tercatat tiga dari lima transaksi. Itu temuan dari sampel kecil ini, bukan bukti semua orang paling suka Nasi Ayam.",
    kind: "chart",
  },
  {
    from: 630,
    duration: 270,
    overlay: "Pola bukan penyebab",
    dialogue:
      "Kita belum tahu alasannya. Tidak ada data harga, promo, atau jumlah pengunjung. Jadi jangan menebak penyebab.",
    kind: "boundary",
  },
  {
    from: 900,
    duration: 270,
    overlay: "Bantu susun. Tetap cek.",
    dialogue:
      "Aku minta Gemini membantu merapikan temuan dan batasnya. Setelah itu, aku cek lagi apakah angkanya sesuai data.",
    kind: "gemini",
  },
  {
    from: 1170,
    duration: 180,
    overlay: "Tanya → cek → ceritakan",
    dialogue: "Coba mulai dari satu pertanyaan. Biar angka punya cerita, dengan bukti.",
    kind: "outro",
  },
] as const;

const CampusBackground: React.FC = () => (
  <AbsoluteFill
    style={{
      background:
        "linear-gradient(180deg, #d8eaff 0%, #f5f8fc 43%, #f3e8d4 43%, #ead8bd 100%)",
    }}
  >
    <div
      style={{
        position: "absolute",
        top: 135,
        left: 80,
        width: 340,
        height: 390,
        border: "18px solid #ffffff",
        borderRadius: 24,
        background:
          "linear-gradient(180deg, #a9d8f8 0%, #dff3ff 68%, #98c58d 68%)",
        boxShadow: "0 18px 45px rgba(24, 48, 74, 0.12)",
      }}
    />
    <div
      style={{
        position: "absolute",
        top: 555,
        left: 0,
        right: 0,
        height: 24,
        background: "rgba(255,255,255,0.6)",
      }}
    />
    <div
      style={{
        position: "absolute",
        bottom: 0,
        left: 0,
        right: 0,
        height: 560,
        background: "linear-gradient(180deg, #f3e8d4 0%, #dfc7a6 100%)",
      }}
    />
  </AbsoluteFill>
);

const Raka: React.FC = () => (
  <svg
    viewBox="0 0 300 500"
    style={{
      position: "absolute",
      left: 40,
      bottom: 290,
      width: 300,
      height: 500,
      filter: "drop-shadow(0 18px 22px rgba(24, 48, 74, 0.16))",
    }}
    aria-label="Ilustrasi Raka, mahasiswa laki-laki"
  >
    <ellipse cx="153" cy="480" rx="112" ry="18" fill="rgba(24,48,74,0.12)" />
    <path d="M75 310 Q150 265 228 310 L270 470 L36 470 Z" fill="#4b7bec" />
    <path d="M112 300 L151 362 L191 300" fill="#ffffff" />
    <rect x="131" y="235" width="42" height="73" rx="18" fill="#d79c73" />
    <ellipse cx="152" cy="173" rx="82" ry="100" fill="#e7b08a" />
    <path
      d="M72 166 Q58 86 122 67 Q196 42 233 100 Q251 128 234 164 Q221 138 201 127 Q162 151 97 136 Q91 153 72 166Z"
      fill="#25364a"
    />
    <path d="M111 179 Q127 166 142 179" fill="none" stroke="#573d33" strokeWidth="7" strokeLinecap="round" />
    <path d="M163 179 Q178 166 194 179" fill="none" stroke="#573d33" strokeWidth="7" strokeLinecap="round" />
    <ellipse cx="128" cy="194" rx="6" ry="8" fill="#18304a" />
    <ellipse cx="180" cy="194" rx="6" ry="8" fill="#18304a" />
    <path d="M137 226 Q153 238 171 224" fill="none" stroke="#9e5e50" strokeWidth="6" strokeLinecap="round" />
    <path d="M40 378 Q12 373 14 407 L35 428 L66 400" fill="#e7b08a" />
    <path d="M231 378 Q261 371 276 400 L260 426 L225 402" fill="#e7b08a" />
  </svg>
);

const BrandMark: React.FC<{ logoAsset: string | null }> = ({ logoAsset }) => (
  <div
    style={{
      position: "absolute",
      top: 70,
      right: 56,
      zIndex: 5,
      minWidth: 180,
      minHeight: 62,
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      padding: "8px 14px",
      borderRadius: 16,
      background: "rgba(255,255,255,0.92)",
      border: logoAsset ? "none" : "2px dashed #7b8ba0",
      color: COLORS.ink,
      fontSize: 18,
      fontWeight: 700,
      textAlign: "center",
    }}
  >
    {logoAsset ? (
      <Img
        src={staticFile(logoAsset)}
        style={{ maxWidth: 210, maxHeight: 70, objectFit: "contain" }}
      />
    ) : (
      "Logo Gemini Academy"
    )}
  </div>
);

const SceneShell: React.FC<SceneProps> = ({ overlay, dialogue, children }) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 12], [0, 1], {
    extrapolateRight: "clamp",
  });
  const translateY = interpolate(frame, [0, 12], [28, 0], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{ opacity }}>
      <div
        style={{
          position: "absolute",
          top: 175,
          right: 55,
          width: 630,
          minHeight: 190,
          padding: "34px 38px",
          borderRadius: 30,
          background: COLORS.white,
          color: COLORS.ink,
          fontFamily: "Arial, sans-serif",
          fontSize: 48,
          fontWeight: 800,
          lineHeight: 1.12,
          boxShadow: "0 20px 60px rgba(24, 48, 74, 0.15)",
          transform: `translateY(${translateY}px)`,
        }}
      >
        {overlay}
      </div>
      {children}
      <div
        style={{
          position: "absolute",
          left: 56,
          right: 56,
          bottom: 70,
          minHeight: 200,
          padding: "28px 34px",
          borderRadius: 26,
          background: "rgba(24, 48, 74, 0.94)",
          color: COLORS.white,
          fontFamily: "Arial, sans-serif",
          fontSize: 34,
          lineHeight: 1.32,
          fontWeight: 600,
          display: "flex",
          alignItems: "center",
          boxShadow: "0 18px 44px rgba(24, 48, 74, 0.18)",
        }}
      >
        {dialogue}
      </div>
    </AbsoluteFill>
  );
};

const TransactionCards: React.FC = () => (
  <div
    style={{
      position: "absolute",
      top: 470,
      right: 55,
      width: 630,
      display: "grid",
      gridTemplateColumns: "1fr 1fr",
      gap: 16,
      fontFamily: "Arial, sans-serif",
    }}
  >
    {["Nasi Ayam", "Mie Ayam", "Nasi Ayam", "Es Teh", "Nasi Ayam"].map(
      (menu, index) => (
        <div
          key={`${menu}-${index}`}
          style={{
            padding: "24px 22px",
            borderRadius: 22,
            background: index === 4 ? COLORS.yellow : COLORS.white,
            color: COLORS.ink,
            fontSize: 28,
            fontWeight: 700,
            boxShadow: "0 12px 30px rgba(24, 48, 74, 0.1)",
          }}
        >
          <span style={{ color: COLORS.muted, fontSize: 18 }}>
            Transaksi {index + 1}
          </span>
          <br />
          {menu}
        </div>
      ),
    )}
    <div
      style={{
        gridColumn: "1 / -1",
        color: COLORS.muted,
        fontFamily: "Arial, sans-serif",
        fontSize: 19,
        fontWeight: 700,
        textAlign: "right",
      }}
    >
      DATA SINTETIS
    </div>
  </div>
);

const BarChart: React.FC = () => (
  <div
    style={{
      position: "absolute",
      top: 475,
      right: 55,
      width: 630,
      height: 450,
      padding: 28,
      borderRadius: 26,
      background: COLORS.white,
      boxShadow: "0 18px 48px rgba(24, 48, 74, 0.12)",
      display: "flex",
      alignItems: "flex-end",
      justifyContent: "space-around",
      fontFamily: "Arial, sans-serif",
    }}
  >
    {[
      { label: "Nasi Ayam", value: 3, color: COLORS.blue },
      { label: "Mie Ayam", value: 1, color: COLORS.green },
      { label: "Es Teh", value: 1, color: "#f0a44b" },
    ].map(({ label, value, color }) => (
      <div
        key={label}
        style={{
          width: 160,
          display: "flex",
          alignItems: "center",
          flexDirection: "column",
          gap: 12,
          color: COLORS.ink,
          fontSize: 22,
          fontWeight: 700,
          textAlign: "center",
        }}
      >
        <span style={{ fontSize: 30 }}>{value}</span>
        <div
          style={{
            width: 110,
            height: 70 + value * 70,
            borderRadius: "18px 18px 6px 6px",
            background: color,
          }}
        />
        <span>{label}</span>
      </div>
    ))}
  </div>
);

const Speculation: React.FC = () => (
  <div
    style={{
      position: "absolute",
      top: 540,
      right: 65,
      width: 600,
      padding: "44px 38px",
      borderRadius: 28,
      background: COLORS.white,
      color: COLORS.ink,
      fontFamily: "Arial, sans-serif",
      fontSize: 40,
      fontWeight: 800,
      textAlign: "center",
      transform: "rotate(-2deg)",
      boxShadow: "0 20px 48px rgba(24, 48, 74, 0.14)",
    }}
  >
    <span style={{ textDecoration: "line-through", textDecorationColor: "#e05a5a" }}>
      Karena lebih murah?
    </span>
    <div style={{ marginTop: 22, color: "#c94949", fontSize: 26 }}>
      Belum ada datanya
    </div>
  </div>
);

const GeminiPromptCard: React.FC = () => (
  <div
    style={{
      position: "absolute",
      top: 470,
      right: 55,
      width: 630,
      padding: 32,
      borderRadius: 26,
      background: COLORS.white,
      color: COLORS.ink,
      fontFamily: "Arial, sans-serif",
      boxShadow: "0 18px 48px rgba(24, 48, 74, 0.12)",
    }}
  >
    <div style={{ color: COLORS.blue, fontSize: 22, fontWeight: 800 }}>
      PROMPT
    </div>
    <div style={{ marginTop: 18, fontSize: 32, fontWeight: 700, lineHeight: 1.25 }}>
      Ringkas pola dari data ini. Pisahkan fakta dan dugaan. Jangan menambah angka.
    </div>
  </div>
);

const SceneVisual: React.FC<{ kind: (typeof scenes)[number]["kind"] }> = ({
  kind,
}) => {
  if (kind === "transactions") return <TransactionCards />;
  if (kind === "chart") return <BarChart />;
  if (kind === "boundary") return <Speculation />;
  if (kind === "gemini") return <GeminiPromptCard />;
  if (kind === "outro") {
    return (
      <div
        style={{
          position: "absolute",
          top: 500,
          right: 55,
          width: 630,
          padding: 38,
          borderRadius: 28,
          background: COLORS.white,
          color: COLORS.ink,
          fontFamily: "Arial, sans-serif",
          fontSize: 34,
          fontWeight: 800,
          textAlign: "center",
          lineHeight: 1.35,
          boxShadow: "0 18px 48px rgba(24, 48, 74, 0.12)",
        }}
      >
        KULIK DATA
        <br />
        WITH GEMINI
      </div>
    );
  }
  return (
    <div
      style={{
        position: "absolute",
        top: 520,
        right: 120,
        width: 500,
        height: 230,
        borderRadius: 28,
        background: COLORS.paleBlue,
        display: "grid",
        placeItems: "center",
        color: COLORS.blue,
        fontFamily: "Arial, sans-serif",
        fontSize: 110,
        fontWeight: 900,
      }}
    >
      ?
    </div>
  );
};

const StoryScene: React.FC<SceneProps & { kind: (typeof scenes)[number]["kind"] }> = ({
  overlay,
  dialogue,
  kind,
}) => (
  <SceneShell overlay={overlay} dialogue={dialogue}>
    <Raka />
    <SceneVisual kind={kind} />
  </SceneShell>
);

export const ShortVideo: React.FC<ShortVideoProps> = ({
  logoAsset,
  voiceoverAsset,
}) => (
  <AbsoluteFill style={{ backgroundColor: COLORS.cream }}>
    <CampusBackground />
    <BrandMark logoAsset={logoAsset} />
    {scenes.map((scene) => (
      <Sequence
        key={scene.kind}
        from={scene.from}
        durationInFrames={scene.duration}
      >
        <StoryScene
          overlay={scene.overlay}
          dialogue={scene.dialogue}
          kind={scene.kind}
        />
      </Sequence>
    ))}
    {voiceoverAsset ? <Audio src={staticFile(voiceoverAsset)} /> : null}
  </AbsoluteFill>
);
