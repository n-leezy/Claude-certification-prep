import React from "react";
import {
  AbsoluteFill, Audio, Sequence, useCurrentFrame, useVideoConfig,
  interpolate, spring, staticFile,
} from "remotion";

export type Point = { t: number; head: string; body: string };
export type LessonData = {
  tag: string; title: string; accent: string; audio: string;
  points: Point[]; durationInSeconds: number;
};

const BG = "#0f1115";
const INK = "#e8eaed";
const MUTED = "#9aa3af";
const PANEL = "#181b22";

const Header: React.FC<{ data: LessonData }> = ({ data }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const e = spring({ frame, fps, config: { damping: 200 } });
  const y = interpolate(e, [0, 1], [-40, 0]);
  const op = interpolate(e, [0, 1], [0, 1]);
  return (
    <div style={{ transform: `translateY(${y}px)`, opacity: op, padding: "56px 64px 0" }}>
      <div style={{ color: data.accent, fontWeight: 800, letterSpacing: 4, fontSize: 22, textTransform: "uppercase" }}>
        {data.tag}
      </div>
      <div style={{ color: INK, fontWeight: 800, fontSize: 50, marginTop: 10, lineHeight: 1.1 }}>
        {data.title}
      </div>
      <div style={{ height: 5, width: 120, background: data.accent, borderRadius: 99, marginTop: 18 }} />
    </div>
  );
};

const Card: React.FC<{ p: Point; accent: string }> = ({ p, accent }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const e = spring({ frame, fps, config: { damping: 200, stiffness: 120 } });
  const x = interpolate(e, [0, 1], [60, 0]);
  const op = interpolate(e, [0, 1], [0, 1]);
  return (
    <div style={{
      transform: `translateX(${x}px)`, opacity: op,
      background: PANEL, border: `1px solid #2c313c`, borderLeft: `5px solid ${accent}`,
      borderRadius: 16, padding: "26px 30px", margin: "0 64px",
    }}>
      <div style={{ color: INK, fontWeight: 700, fontSize: 36 }}>{p.head}</div>
      <div style={{ color: MUTED, fontSize: 26, marginTop: 10, lineHeight: 1.4 }}>{p.body}</div>
    </div>
  );
};

const Progress: React.FC<{ accent: string }> = ({ accent }) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const w = interpolate(frame, [0, durationInFrames], [0, 100], { extrapolateRight: "clamp" });
  return (
    <div style={{ position: "absolute", bottom: 0, left: 0, right: 0, height: 6, background: "#21252e" }}>
      <div style={{ height: "100%", width: `${w}%`, background: accent }} />
    </div>
  );
};

export const Lesson: React.FC<{ data: LessonData }> = ({ data }) => {
  const { fps } = useVideoConfig();
  return (
    <AbsoluteFill style={{ background: BG, fontFamily: "Helvetica, Arial, sans-serif" }}>
      <Audio src={staticFile(data.audio)} />
      <Header data={data} />
      <AbsoluteFill style={{ justifyContent: "center", marginTop: 70 }}>
        {data.points.map((p, i) => {
          const start = Math.round(p.t * fps);
          const next = data.points[i + 1] ? Math.round(data.points[i + 1].t * fps) : Number.MAX_SAFE_INTEGER;
          return (
            <Sequence key={i} from={start} durationInFrames={next - start}>
              <AbsoluteFill style={{ justifyContent: "center" }}>
                <Card p={p} accent={data.accent} />
              </AbsoluteFill>
            </Sequence>
          );
        })}
      </AbsoluteFill>
      <div style={{ position: "absolute", bottom: 22, left: 64, color: MUTED, fontSize: 18 }}>
        CCA-F prep · unofficial community material
      </div>
      <Progress accent={data.accent} />
    </AbsoluteFill>
  );
};
