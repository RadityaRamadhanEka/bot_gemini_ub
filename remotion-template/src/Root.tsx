import React from "react";
import { Composition } from "remotion";
import { ShortVideo } from "./ShortVideo";

const defaultProps = {
  logoAsset: null,
  voiceoverAsset: null,
};

export const Root: React.FC = () => {
  return (
    <Composition
      id="KulikDataEpisode12"
      component={ShortVideo}
      durationInFrames={1350}
      fps={30}
      width={1080}
      height={1920}
      defaultProps={defaultProps}
    />
  );
};
